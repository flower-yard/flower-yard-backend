from django_filters.rest_framework import FilterSet, filters

from flower.models import Category, Product


class CategoriesFilter(FilterSet):
    """
    Фильтрация по категориям. Фильтруются по категорям
    без дочерних категорий
    """
    child = filters.BooleanFilter(
        method='get_get_not_child'
    )

    class Meta:
        models = Category
        fields = (
            'child'
        )

    def get_get_not_child(self, *args, **kwargs):
        if self.data.get('child') == 'False':
            return self.queryset.filter(
                parent=None
            )
        return self.queryset


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
            'badge'
        )


