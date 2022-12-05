from django.db import models
from locations import get_location
class Client(models.Model):
    name = models.CharField(max_length=100,verbose_name="Client name",help_text="Enter client name",null=True,blank=True)
    username = models.CharField(max_length=100,verbose_name="Client username",help_text="Enter client username",null=True,blank=True)
    telegram_id = models.CharField(max_length=30,verbose_name="Telegram ID",help_text="Enter telegram ID",unique=True)
    language = models.CharField(max_length=10,default="uz",verbose_name="Client System Language",help_text="Enter client system language")
    phone = models.CharField(max_length=100,verbose_name="Client Phone Number",help_text="Enter client phone",null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.telegram_id} IDli foydalanuvchi"
    class Meta:
        db_table="Cleints"
        verbose_name='Client '
        verbose_name_plural="Clients "
class Address(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE,to_field='telegram_id',related_name='address')
    latitude = models.CharField(max_length=50,verbose_name="Client latitude",help_text="Enter client latitude")
    longitude =  models.CharField(max_length=50,verbose_name="Client longitude",help_text="Enter client longitude")
    def __str__(self):
        data=get_location(latitude=self.latitude,longitude=self.longitude)
        return data[10:]
    class Meta:
        db_table = "Address"
        verbose_name = "Address "
        verbose_name_plural="Address "
    @property
    def adres(self):
        data=get_location(latitude=self.latitude,longitude=self.longitude)
        return data[10:]