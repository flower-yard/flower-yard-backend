from django.db.models import F
from django.db.transaction import atomic

from flower.models import Product


def _calculate_number_products(products) -> None:
    """Производит вычитание количества товара."""
    with atomic():
        for product in products:
            obj = Product.objects.get(pk=product['id'])
            obj.amount = F('amount') - product['count']
            obj.save()
