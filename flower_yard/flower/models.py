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


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=350
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=100,
        unique=True
    )
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='child'
    )


class Flower(models.Model):
    badge = models.OneToOneField(
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
    name = models.CharField(
        verbose_name='',
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
    price = models.IntegerField(
        verbose_name='Цена, руб.',
        validators=[
            validators.MinValueValidator(
                0, message='Введите значение больше 0'
            )
        ]
    )


class Characteristic(models.Model):
    flower = models.ManyToManyField(
        Flower,
        through='FlowerCharacteristic'
    )
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


class Badge(models.Model):
    name = models.CharField(
        verbose_name='Название бейджа',
        max_length=50,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=50,
        unique=True
    )


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
