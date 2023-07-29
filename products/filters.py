from . models import Product
import django_filters
from django_filters.filters import RangeFilter

# Creating product filters
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = RangeFilter()


    class Meta:
        model = Product
        fields = ['name', 'price']