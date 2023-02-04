import re

from django import forms
from rest_framework import serializers
from django.core.exceptions import ValidationError


def isEmailAddressValid(email: str):
    """Проверяет правильность введенного email."""
    try:
        forms.EmailField().clean(email)
        return email
    except ValidationError:
        raise serializers.ValidationError({'email': 'Неверный email!'})


def isPhoneValid(phone: str):
    """Проверяет правильность введенного номера телефона."""
    r = re.compile(
        '^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$'
    )
    if not r.search(phone):
        raise serializers.ValidationError(
            {'phone': f'Некоректный номер - {phone}'}
        )
    return phone
