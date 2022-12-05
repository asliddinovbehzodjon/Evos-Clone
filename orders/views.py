from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.views import APIView
from .serializers import *
class ShopInfo(APIView):
    def get(self,request,telegram_id):
        datas = Order.objects.get(client=telegram_id)
        objects = datas.orderitem_set.all()
        objects =objects.values()
        return Response(data=objects,status=status.HTTP_200_OK)
class Shoppping(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        datas = Order.objects.filter(client=params['pk'])
        serializer = OrderSerializer(datas,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class Add(APIView):
    def get(self,request,telegram_id,product):
        order = Order.objects.get(client=telegram_id)
        product= Product.objects.get(id=product)
        items =OrderItem.objects.filter(order=order,product=product)
        if items.exists():
             item =OrderItem.objects.get(order=order,product=product)
             
             item.quantity = item.quantity+1
             item.save()
        else:
            OrderItem.objects.create(order=order,product=product)
        return Response({'status':'Ok'})
class Remove(APIView):
    def get(self,request,telegram_id,product):
        order = Order.objects.get(client=telegram_id)
        product= Product.objects.get(id=product)
        item =OrderItem.objects.get(order=order,product=product)
        if item.quantity>1:
            item.quantity = item.quantity-1
            item.save()
        else:
            item.delete()
        
        return Response({'status':'Ok'})
    
        