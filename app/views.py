from django.shortcuts import render
from .models import *
from .serializers import *
from django_filters.rest_framework import  DjangoFilterBackend
from .filters import ProductFilter,CategoryFilter
# Create your views here.
from rest_framework.viewsets import ModelViewSet
class Categories(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class =CategoryFilter
class Products(ModelViewSet):
    queryset =Product.objects.all()
    serializer_class =ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class =ProductFilter
