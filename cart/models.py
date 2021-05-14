from django.db import models

from cereal.models import Cereal
from user.models import User

COUNTRIES = (
    ('US', 'United States'),
    ('FR', 'France'),
    ('CN', 'China'),
    ('RU', 'Russia'),
    ('IS', 'Iceland'),
)


# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=32)
    street_name = models.CharField(max_length=32)
    house_number = models.IntegerField()
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32, choices=COUNTRIES)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Cereal, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ['item']

    def __str__(self):
        return f"{self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(BillingAddress, on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
