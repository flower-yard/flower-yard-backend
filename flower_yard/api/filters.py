from django_filters.rest_framework import FilterSet, filters
from django.db.models import Q

from flower.models import Category, Product


class CategoriesFilter(FilterSet):
    """
    Фильтрация по категориям.
    """
    name = filters.CharFilter(method='get_get_name') # Чувстивтелен к регистру из-за того, что
    slug = filters.CharFilter(lookup_expr='istartswith') # SQLite, в интернетах пишут, что с Postgre будет норм
    child = filters.BooleanFilter(
        method='get_get_not_child'
    )

    class Meta:
        models = Category
        fields = (
            'name',
            'slug',
            'child',
        )

    def get_get_not_child(self, *args, **kwargs):
        if self.data.get('child') == 'False':
            return self.queryset.filter(
                parent=None
            )
        return self.queryset

    def get_get_name(self, *args, **kwargs):
        return self.queryset.filter(
            Q(name__istartswith=self.data.get('name')) | Q(parent__name__istartswith=self.data.get('name'))
        )


class FlowerFilter(FilterSet):
    """
    Фильтрация по товарам.
    """
    name = filters.CharFilter(lookup_expr='istartswith')
    badge = filters.CharFilter(field_name='badge__slug')

    class Meta:
        model = Product
        fields = (
            'name',
            'badge',
            'category'
        )


