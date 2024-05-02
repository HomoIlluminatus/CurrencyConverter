from rest_framework import serializers

from .models import CurrencyRate

class CurrencyRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CurrencyRate
        fields = '__all__'
        
class CurrencyConversionResponseSerializer(serializers.Serializer):
    original_amount = serializers.DecimalField(max_digits=10, decimal_places=8)
    from_currency = serializers.CharField(max_length=3)
    converted_amount = serializers.DecimalField(max_digits=10, decimal_places=8)
    to_currency = serializers.CharField(max_length=3)
    timestamp = serializers.DateTimeField()