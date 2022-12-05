from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('clients',ClientViewset)
router.register('address',AddressViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('language/<int:telegram_id>/',LanguageView.as_view()),
    path('changelanguage/<int:telegram_id>/<str:language>/',ChangeLanguageView.as_view()),
    path('manzil/<int:telegram_id>/',AddressView.as_view())
]
