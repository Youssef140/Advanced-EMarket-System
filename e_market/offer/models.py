from datetime import datetime
from django.db import models
from listings.models import Product

currency_choices = (
    ('usd', 'USD'),
    ('lbp', 'LBP')
)


class Offer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=25)
    currency = models.CharField(max_length=10, choices=currency_choices, default='lbp')
    from_date = models.DateTimeField(default=datetime.now,blank=True)
    to_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name


class Offer_Product(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)