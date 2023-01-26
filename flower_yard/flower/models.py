from django.core import validators
from django.db import models


class LightLoving(models.IntegerChoices):
    SHADOW = 1, 'Тень'
    PENUMBRA = 2, 'Полутень'
    LIGHT = 3, 'Свет'


class FlowingPeriod(models.IntegerChoices):
    APRIL = 4, 'Апрель'
    MAY = 5, 'Май'
    JUNE = 6, 'Июнь'
    JULY = 7, 'Июль'
    AUGUST = 8, 'Август'
    SEPTEMBER = 9, 'Сентябрь'
    OCTOBER = 10, 'Октябрь'
    NOVEMBER = 11, 'Ноябрь'
    __empty__ = 'Выберите месяц'


class CategoryBadgeBase(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=350
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=100,
        unique=True
    )

    class Meta:
        abstract = True


class Category(CategoryBadgeBase):
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='child'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'Category'

    def __str__(self):
        return self.name


class Flower(models.Model):
    badge = models.ForeignKey(
        'Badge',
        on_delete=models.SET_NULL,
        related_name='flower_badge',
        blank=True,
        null=True,
        verbose_name='Бейдж'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category',
        verbose_name='Категория'
    )
    flowers = models.ManyToManyField(
        'Characteristic',
        through='FlowerCharacteristic'
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=300,
        db_index=True
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        verbose_name='Фото растения',
        upload_to='flowers/'
    )
    price = models.DecimalField(
        verbose_name='Цена, руб.',
        max_digits=10,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(
                0, message='Введите значение больше 0'
            )
        ]
    )

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'
        db_table = 'Flower'

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    height = models.DecimalField(
        verbose_name='Высота, см',
        max_digits=10,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(
                0, message='Введите значение больше 0'
            )
        ]
    )
    diameter = models.DecimalField(
        verbose_name='Диаметр, см',
        max_digits=10,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(
                0, message='Введите значение больше 0'
            )
        ]
    )
    weight = models.DecimalField(
        verbose_name='Вес, кг',
        max_digits=10,
        decimal_places=3,
        validators=[
            validators.MinValueValidator(
                0, message='Введите значение больше 0'
            )
        ]
    )
    light_loving = models.SmallIntegerField(
        verbose_name='Выбор светолюбивости',
        choices=LightLoving.choices,
        blank=True
    )
    period_from = models.SmallIntegerField(
        verbose_name='Цветение с',
        choices=FlowingPeriod.choices,
        default=FlowingPeriod.MAY
    )
    period_by = models.SmallIntegerField(
        verbose_name='Цветение по',
        choices=FlowingPeriod.choices,
        default=FlowingPeriod.OCTOBER
    )

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
        db_table = 'Characteristic'

    def __str__(self):
        return f'высота - {self.height} см, диаметр - {self.diameter} см'


class FlowerCharacteristic(models.Model):
    characteristics = models.ForeignKey(
        Characteristic,
        on_delete=models.CASCADE,
        related_name='char_flower',
        verbose_name='Характеристика'
    )
    flowers = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
        related_name='flower_char',
        verbose_name='Растение'
    )

    class Meta:
        db_table = 'FlowerCharacteristic'

    def __str__(self):
        return f'{self.flowers}: {self.characteristics}'


class Badge(CategoryBadgeBase):
    class Meta:
        verbose_name = 'Бейдж'
        verbose_name_plural = 'Бейджи'
        db_table = 'Badge'

    def __str__(self):
        return {self.name}


class QR(models.Model):
    flower = models.OneToOneField(
        Flower,
        on_delete=models.CASCADE,
        related_name='flower_qr',
        verbose_name='Растение'
    )
    url = models.URLField(
        verbose_name='Интернет ресурс на растение'
    )

    class Meta:
        verbose_name = 'QR-код'
        verbose_name_plural = 'QR-коды'
        db_table = 'QR'

    def __str__(self):
        return f'{self.flower:}: {self.url}'
