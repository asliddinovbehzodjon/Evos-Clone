from rest_framework import serializers
from .models import *
class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['order','quantity','product']
   
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    all_items = serializers.SerializerMethodField('all_products')
    all_cost = serializers.SerializerMethodField('all_summa')
    class Meta:
        model = Order
        fields = ["client",'items','all_items','all_cost']
        # depth =1
    def all_products(self,order):
        total = order.all_items
        return total
    def all_summa(self,order):
        total = order.all_cost
        return total