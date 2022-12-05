from django.contrib import admin

# Register your models here.
from .models import Client,Address
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','telegram_id','language','phone']
    list_filter  = ['language','created']
    search_fields = ['name','telegram_id','phone']
    list_per_page = 10
    list_max_show_all = 15
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['adres','client']
    search_fields = ['adres','client']
    list_per_page = 10
    list_max_show_all = 15
    