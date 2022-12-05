from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('shop',Shoppping)
urlpatterns = [
    path('',include(router.urls)),
    path('shopping/<int:telegram_id>/',ShopInfo.as_view()),
    path('add/<int:telegram_id>/<int:product>/',Add.as_view()),
    path('remove/<int:telegram_id>/<int:product>/',Remove.as_view())
]
