from django.contrib import admin

# Register your models here.
from .models import Order,OrderItem
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product','order']
    list_per_page = 10 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client','user','all_cost','all_items']
    list_per_page = 10
    search_fields = ['client__name','client__telegram_id']