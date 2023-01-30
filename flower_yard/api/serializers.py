from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from flower.models import (Badge, Category, Characteristic,
                           Flower, FlowerCharacteristic,
                           FlowingPeriod,  LightLoving)


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


class FlowerSerializer(serializers.ModelSerializer):
    badge = SlugRelatedField(
        slug_field='name', read_only=True
    )
    category = SlugRelatedField(
        slug_field='name', read_only=True)

    class Meta:
        model = Flower
        fields = (
            'id',
            'badge',
            'category',
            'name',
            'description',
            'image',
            'price'
        )


class CharacteristicSerializer(serializers.ModelSerializer):
    light_loving = serializers.ChoiceField(choices=LightLoving.choices)
    period_from = serializers.ChoiceField(choices=FlowingPeriod.choices)
    period_by = serializers.ChoiceField(choices=FlowingPeriod.choices)

    class Meta:
        model = Characteristic
        fields = (
            'id',
            'height',
            'diameter',
            'weight',
            'light_loving',
            'period_from',
            'period_by'
        )


class FlowerCharacteristicSerializer(serializers.ModelSerializer):
    flowers = FlowerSerializer()
    characteristics = CharacteristicSerializer()

    class Meta:
        model = FlowerCharacteristic
        fields = (
            'flowers',
            'characteristics'
        )

