from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from flower.models import Badge, Category, Characteristic, Flower


class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge
        fields = (
            'name',
            'slug'
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'parent_category'
        )


class ReadFlowerSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer
    category = CategorySerializer

    class Meta:
        model = Flower
        fields = (
            'badge',
            'category',
            'name',
            'description',
            'image',
            'price'
        )


class FlowerSerializer(serializers.ModelSerializer):
    badge = SlugRelatedField(
        slug_field='slug', queryset=Badge.objects.all(),
    )
    category = SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all(),
    )

    class Meta:
        model = Flower
        fields = (
            'badge',
            'category',
            'name',
            'description',
            'image',
            'price'
        )

