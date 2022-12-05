from django.shortcuts import render

# Create your views here.
from rest_framework import routers,status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class LanguageView(APIView):
    def get(self,request,telegram_id):
        objects = list(Client.objects.filter(telegram_id=telegram_id).values('language'))
        return Response(objects,status=status.HTTP_200_OK)
class ChangeLanguageView(APIView):
    def get(self,request,telegram_id,language):
        client = Client.objects.get(telegram_id=telegram_id)
        client.language =language
        client.save()
        return Response({'status':'Ok'})
class AddressView(APIView):
    def get(self,request,telegram_id):
        objects = Client.objects.get(telegram_id=telegram_id)
        data =  objects.address.all()
        data= data.values()
        return Response(data=data,status=status.HTTP_200_OK)
class AddressViewset(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
