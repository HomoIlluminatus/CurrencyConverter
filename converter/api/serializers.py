from rest_framework import serializers

from .models import CurrencyRate


class CurrencyRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CurrencyRate
        fields = "__all__"
        
class CurrencyConversionRequestSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=20, decimal_places=10)
    from_currency = serializers.CharField(max_length=3)
    to_currency = serializers.CharField(max_length=3)
    
    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("amount должно быть положительным числом")
        return amount
        
class CurrencyConversionResponseSerializer(serializers.Serializer):
    original_amount = serializers.DecimalField(max_digits=20, decimal_places=10)
    from_currency = serializers.CharField(max_length=3)
    converted_amount = serializers.DecimalField(max_digits=20, decimal_places=10)
    to_currency = serializers.CharField(max_length=3)
    timestamp = serializers.DateTimeField()