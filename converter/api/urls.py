from django.urls import path

from .views import CurrencyConversionAPIView

app_name = 'api'

urlpatterns = [
    path('api/', CurrencyConversionAPIView.as_view())
]