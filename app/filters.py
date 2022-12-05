from django_filters import FilterSet
from .models import *
class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields ={
            'name':['iexact']
        }

class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields ={
            'name':['iexact']
        }