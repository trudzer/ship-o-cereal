from django.db import models

from cereal.models import Cereal
from user.models import User


# Create your models here.

class OrderItem(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	item = models.ForeignKey(Cereal, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=1)
	class Meta:
		ordering = ['item']

	def __str__(self):
		return f"{self.quantity} of {self.item.name}"

	def get_total_item_price(self):
		return self.quantity * self.item.price


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def get_total(self):
		total = 0
		for order_item in self.items.all():
			total += order_item.get_total_item_price()
		return total