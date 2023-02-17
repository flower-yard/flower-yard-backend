from rest_framework import serializers

from api.utils import ValueField
from flower.models import (Badge, Category, Characteristic,
                           Documents, Product, ProductCharacteristic)


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = (
            'name',
            'slug'
        )


class ProductViewSerializer(serializers.ModelSerializer):
    """Выдает общую информацию о продукте"""
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'image'
        )


class CatalogListSerializer(serializers.ModelSerializer):
    """Выдает все имеющиеся категории."""
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'pk',
            'name',
            'slug',
            'parent'
        )

    def get_parent(self, obj):
        return CatalogListSerializer(
            obj.parent).data if obj.parent else None


class CatalogDetailSerializer(serializers.ModelSerializer):
    """Выдает информацию конкретной категории."""
    products = serializers.SerializerMethodField(source='category')

    class Meta:
        model = Category
        fields = (
            'pk',
            'name',
            'slug',
            'products'
        )

    def get_products(self, category):
        request = self.context.get('request')
        sorted_badge = request.query_params.get('sorted_badge')
        if sorted_badge:
            return ProductViewSerializer(
                Product.objects.filter(category=category, badge__slug=sorted_badge),
                context={'queryset': request},
                many=True
            ).data
        return ProductViewSerializer(
            Product.objects.filter(category=category),
            context={'queryset': request},
            many=True
        ).data


class CharacteristicSerializer(serializers.ModelSerializer):
    value = ValueField(
        source='char_product',
        queryset=ProductCharacteristic.objects.all()
    )

    class Meta:
        model = Characteristic
        fields = ('name', 'value')


class ProductDetailSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer()
    category = CatalogListSerializer()
    characteristics = CharacteristicSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'badge',
            'category',
            'characteristics',
            'name',
            'description',
            'image',
            'price',
            'amount'
        )


class DocumentsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_filename')
    download = serializers.FileField(source='file')

    class Meta:
        model = Documents
        fields = (
            'name',
            'download',
        )

    def get_filename(self, obj, *args, **kwargs):
        return str(obj).split('/')[-1]
