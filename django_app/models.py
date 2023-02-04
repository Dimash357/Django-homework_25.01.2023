from django.db import models

class CurrencyExchangeRate(models.Model):
    currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateTimeField(auto_now_add=True)
