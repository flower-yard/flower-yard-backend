import re

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from flower.models import Product
from .utils import DocumentProduct


class SendEmailSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=30)
    products = DocumentProduct(allow_empty=True)

    def validate_phone(self, value):
        r = re.compile(
            '^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$'
        )
        if not r.search(value):
            raise serializers.ValidationError(
                {'phone': f'Некоректный номер - {value}'}
            )
        return value

    def validate_products(self, value):
        unique_products = []
        for data in value:
            product = get_object_or_404(Product, pk=data['id'])
            if product in unique_products:
                raise serializers.ValidationError(
                    'Продукт не может повторяться'
                )
            if not product.amount:
                raise serializers.ValidationError(
                    f'{product.name} - закончился!'
                )
            if (product.amount - data['count']) < 0:
                raise serializers.ValidationError(
                    f'{product.name} на складе осталось - {product.amount}'
                )
            unique_products.append(product)
        return value
