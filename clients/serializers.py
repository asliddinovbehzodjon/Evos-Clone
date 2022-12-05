from rest_framework import serializers
from .models import Client,Address
from locations import get_location
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
class AddressSerializer(serializers.ModelSerializer):
    manzillar = serializers.SerializerMethodField('manzil')
    class Meta:
        model = Address
        fields = ['latitude','longitude','manzillar','client']
    def manzil(self,address):
        return get_location(latitude=address.latitude,longitude=address.longitude)