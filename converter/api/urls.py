from django.urls import path

from .views import get_currency_rate

app_name = 'api'

urlpatterns = [
    path('api/', get_currency_rate)
]