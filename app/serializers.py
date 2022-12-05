from rest_framework import serializers
from .models import Category,Product
# Get Categories #
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','image','products']
        depth=1
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','category','price','image','discount','about']
    