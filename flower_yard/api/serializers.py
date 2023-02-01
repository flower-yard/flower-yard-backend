from rest_framework import serializers

from api.utils import ValueField
from flower.models import (
    Badge, Category,
    Characteristic, Product,
    ProductCharacteristic
)


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = (
            'name',
            'slug'
        )


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    def get_parent(self, obj):
        return CategorySerializer(
            obj.parent).data if obj.parent else None

    class Meta:
        model = Category
        fields = (
            'pk',
            'name',
            'slug',
            'parent'
        )


class CharacteristicSerializer(serializers.ModelSerializer):
    value = ValueField(
        source='char_product',
        queryset=ProductCharacteristic.objects.all()
    )

    class Meta:
        model = Characteristic
        fields = ('name', 'value')


class FlowerSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer()
    category = CategorySerializer()
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
