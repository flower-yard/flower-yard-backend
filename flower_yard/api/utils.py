from rest_framework import serializers


class ValueField(serializers.RelatedField):
    """Настройка реляционного поля для value."""
    def to_representation(self, value):
        return value.first().value

    def to_internal_value(self, data):
        return data
