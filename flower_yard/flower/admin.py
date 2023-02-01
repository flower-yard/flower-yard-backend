from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import (
    Category,
    Product,
    Characteristic,
    Badge, Documents, ProductCharacteristic
)


class ProductCharacteristicInline(admin.StackedInline):
    model = ProductCharacteristic
    extra = 3
    verbose_name = 'Наименование характеристики'
    verbose_name_plural = 'Наименование характеристик'


class CategoryAdmin(MPTTModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
        'parent'
    )
    prepopulated_fields = {'slug': ('name',)}
    mptt_level_indent = 20


class FlowerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'image',
        'badge',
        'category',
    )
    inlines = [ProductCharacteristicInline]


class BadgeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug'
    )


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name'
    )


class DocumentsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'file',
        'date_create',
        'date_update'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, FlowerAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.register(Documents, DocumentsAdmin)
