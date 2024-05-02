from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CurrencyRate
from .serializers import CurrencyConversionRequestSerializer, CurrencyConversionResponseSerializer

class CurrencyConversionAPIView(APIView):
    def get(self, request):
        serializer_request = CurrencyConversionRequestSerializer(data=request.data)
        
        if serializer_request.is_valid():
            amount = serializer_request.validated_data['amount']
            from_currency = serializer_request.validated_data['from_currency']
            to_currency = serializer_request.validated_data['to_currency']
            try:
                from_currency_rate = CurrencyRate.objects.get(currency_code=from_currency)
            except CurrencyRate.DoesNotExist:
                return Response(f"Валюта {from_currency} не найдена", status=404)
            try:
                to_currency_rate = CurrencyRate.objects.get(currency_code=to_currency)
            except CurrencyRate.DoesNotExist:
                return Response(f"Валюта {to_currency} не найдена", status=404)
            
            from_exchange_rate = from_currency_rate.exchange_rate
            to_exchange_rate = to_currency_rate.exchange_rate
            
            converted_amount = round(amount * to_exchange_rate / from_exchange_rate, 10)
            print(converted_amount)
            
            response = {
                'original_amount': amount,
                'from_currency': from_currency,
                'converted_amount': converted_amount,
                'to_currency': to_currency,
                'timestamp': datetime.now()
            }
            serializer_response = CurrencyConversionResponseSerializer(response)
            return Response(serializer_response.data, status=200)
        return Response(serializer_request.errors, status=400)