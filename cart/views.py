from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import View
from cart.models import OrderItem, Order
from cereal.models import Cereal
from django.contrib import messages

@login_required
def add_to_cart(request, id):
	item = get_object_or_404(Cereal, pk=id)
	order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__id=item.id).exists():
			order_item.quantity += 1
			order_item.save()
			messages.info(request, "This item was added to your cart.")
			return redirect("http://127.0.0.1:8000/cereals/")
		else:
			messages.info(request, "This item was added to your cart.")
			order.items.add(order_item)
			return redirect("http://127.0.0.1:8000/cereals/")
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=ordered_date)
		order.items.add(order_item)
		messages.info(request, "This item was added to your cart.")
		return redirect("http://127.0.0.1:8000/cereals/")

@login_required
def add_to_cart_in_cart(request, id):
	item = get_object_or_404(Cereal, pk=id)
	order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__id=item.id).exists():
			order_item.quantity += 1
			order_item.save()
			messages.info(request, "This item was added to your cart.")
			return redirect('http://127.0.0.1:8000/cart/')
		else:
			messages.info(request, "This item was added to your cart.")
			order.items.add(order_item)
			return redirect('http://127.0.0.1:8000/cart/')
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=ordered_date)
		order.items.add(order_item)
		messages.info(request, "This item was added to your cart.")
		return redirect('http://127.0.0.1:8000/cart/')


def remove_single_item_from_cart(request, id):
	item = get_object_or_404(Cereal, pk=id)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__id=item.id).exists():
			order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
			if order_item.quantity > 1:
				order_item.quantity -= 1
				order_item.save()
			else:
				order_item.delete()
			messages.info(request, "This item quantity was reduced.")
			return redirect('http://127.0.0.1:8000/cart/')
		else:
			messages.info(request, "This item was not in your cart.")
			return redirect('http://127.0.0.1:8000/cart/')
	else:
		messages.info(request, "You do not have an order.")
		return redirect('http://127.0.0.1:8000/cart/')

def clear_cart(request, id):
	item = get_object_or_404(Cereal, pk=id)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__id=item.id).exists():
			order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
			order_item.delete()
			messages.info(request, "This item was removed from your cart.")
			return redirect('http://127.0.0.1:8000/cart/')
		else:
			messages.info(request, "This item was not in your cart.")
			return redirect('http://127.0.0.1:8000/cart/')
	else:
		messages.info(request, "You do not have an order.")
		return redirect('http://127.0.0.1:8000/cart/')

class Cart_View(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		try:
			order = Order.objects.get(user=self.request.user, ordered=False)
			context = {
				'object': order
			}
			return render(self.request, 'cart/cart.html', context)
		except ObjectDoesNotExist:
			messages.error(self.request, "You do not have an active order")
			return redirect("/")
		return render(self.request, 'cart/cart.html')

def checkout(request):
	return render(request, 'cart/checkout.html')