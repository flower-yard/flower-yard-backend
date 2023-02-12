from django.core import validators
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

MEASUREMENT = (
    ('cm', 'см'),
    ('mm', 'мм'),
    ('kg', 'кг'),
    ('gr', 'гр')
)


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


class Category(MPTTModel, CategoryBadgeBase):
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='child',
        verbose_name='Родительская категория'
    )
    image = models.ImageField(
        upload_to='catalog/',
        blank=True,
        null=True,
        verbose_name='Картинка'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'Category'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    badge = models.ForeignKey(
        'Badge',
        on_delete=models.SET_NULL,
        related_name='product_badge',
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
    characteristics = models.ManyToManyField(
        'Characteristic',
        through='ProductCharacteristic'
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=300,
        db_index=True
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=100,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        verbose_name='Фото растения',
        upload_to='products/'
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
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество товаров, шт.'
    )
    in_available = models.BooleanField(
        default=True,
        verbose_name='В наличии'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table = 'Product'

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    name = models.CharField(
        max_length=300,
        verbose_name='Наименование характеристики'
    )

    class Meta:
        verbose_name = 'Наименование характеристики'
        verbose_name_plural = 'Наименование характеристик'

    def __str__(self):
        return self.name


class ProductCharacteristic(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_char',
        verbose_name='Продукт'
    )
    characteristic = models.ForeignKey(
        Characteristic,
        on_delete=models.CASCADE,
        related_name='char_product',
        verbose_name='Характеристика'
    )
    value = models.CharField(
        max_length=300,
        verbose_name='Значение характеристики',
    )
    measurement = models.CharField(
        max_length=2,
        choices=MEASUREMENT,
        blank=True,
        null=True,
        verbose_name='Единица измерения'
    )

    class Meta:
        db_table = 'ProductCharacteristic'
        constraints = (
            models.UniqueConstraint(
                fields=('product', 'characteristic'),
                name='unique_product_characteristic',
            ),
        )


class Badge(CategoryBadgeBase):
    class Meta:
        verbose_name = 'Бейдж'
        verbose_name_plural = 'Бейджи'
        db_table = 'Badge'

    def __str__(self):
        return self.name


class Documents(models.Model):
    file = models.FileField(
        upload_to='archives/',
        verbose_name='Документ'
    )
    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата загрузки'
    )
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )

    class Meta:
        get_latest_by = ['date_create', 'date_update']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.file.name
