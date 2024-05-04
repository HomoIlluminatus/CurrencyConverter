from django.db import models


class CurrencyRate(models.Model):
    currency_code = models.CharField(max_length=3, unique=True)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, blank=True)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["currency_code"]
        indexes = [
            models.Index(fields=["currency_code"]),
        ]
    
    def __str__(self):
        return self.currency_code
    
    