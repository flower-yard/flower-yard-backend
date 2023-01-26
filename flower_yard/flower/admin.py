from django.contrib import admin

from .models import Category, Flower, Characteristic, FlowerCharacteristic, Badge, QR


class FlowerCharacteristicInline(admin.StackedInline):
    model = FlowerCharacteristic
    extra = 1
    verbose_name = 'Характеристика'
    verbose_name_plural = 'Характеристики'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
        'parent_category'
    )
    prepopulated_fields = {'slug': ('name',)}


class FlowerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'image',
        'badge',
        'category',
    )
    inlines = [FlowerCharacteristicInline]


class BadgeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug'
    )


class CharacteristicCAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'height',
        'diameter',
        'light_loving'
    )


class QRAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'flower',
        'url'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(Characteristic, CharacteristicCAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.register(QR, QRAdmin)
