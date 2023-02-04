from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin
from .models import (
    Category,
    Product,
    Characteristic,
    Badge, Documents, ProductCharacteristic
)
from mptt.admin import TreeRelatedFieldListFilter

class ProductCharacteristicInline(admin.StackedInline):
    model = ProductCharacteristic
    extra = 3
    verbose_name = 'Характеристика'
    verbose_name_plural = 'Характеристики'


class CategoryAdmin(MPTTModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
        'parent'
    )
    prepopulated_fields = {'slug': ('name',)}
    mptt_level_indent = 20


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'image_tag',
        'badge',
        'category',
        'amount',
        'in_available'
    )
    search_fields = ('name',)
    list_filter = (
        'badge',
        ('category', TreeRelatedFieldListFilter)
    )
    inlines = [ProductCharacteristicInline]

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="width: 35px; height:35px;"/>'.format(
                obj.image.url))

    image_tag.__name__ = 'Фото'


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
admin.site.register(Product, ProductAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.register(Documents, DocumentsAdmin)
