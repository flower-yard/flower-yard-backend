from rest_framework import serializers


class DocumentProduct(serializers.ListField):
    child = serializers.DictField(
        child=serializers.IntegerField(),
        allow_empty=True
    )
