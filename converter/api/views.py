from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import CurrencyRate
from .serializers import CurrencyRateSerializer

@api_view(['GET'])
def get_currency_rate(request):
    amount = request.data.get('amount')
    from_currency = request.data.get('from_currency')
    to_currency = request.data.get('to_currency')
    try:
        exchange_rate_from = CurrencyRate.objects.get(currency_code=from_currency)
        exchange_rate_to = CurrencyRate.objects.get(currency_code=to_currency)
    except CurrencyRate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    serializer = CurrencyRateSerializer(instance=instance)
    return Response(serializer.data)