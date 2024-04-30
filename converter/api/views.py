import io
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .models import CurrencyRate
from .serializers import CurrencyRateSerializer

@api_view(['GET'])
def get_currency_rate(request):
    currency_code = request.data[0]['currency_code']
    instance = CurrencyRate.objects.get(currency_code=currency_code)
    serializer = CurrencyRateSerializer(instance=instance)
    return Response(serializer.data)