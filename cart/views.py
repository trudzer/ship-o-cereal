from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
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
			return render(request, 'cereal/cereal_details.html', {
				'cereal': get_object_or_404(Cereal, pk=id)
			})
		else:
			messages.info(request, "This item was added to your cart.")
			order.items.add(order_item)
			return render(request, 'cereal/cereal_details.html', {
				'cereal': get_object_or_404(Cereal, pk=id)
			})
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=ordered_date)
		order.items.add(order_item)
		messages.info(request, "This item was added to your cart.")
		return render(request, 'cereal/cereal_details.html', {
			'cereal': get_object_or_404(Cereal, pk=id)
		})

def remove_from_cart(request, id):
	item = get_object_or_404(Cereal, pk=id)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__id=item.id).exists():
			order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
			order.items.remove(order_item)
			messages.info(request, "This item was removed from your cart.")
			return render(request, 'cereal/cereal_details.html', {
				'cereal': get_object_or_404(Cereal, pk=id)
			})
		else:
			messages.info(request, "This item was not in your cart.")
			return render(request, 'cereal/cereal_details.html', {
				'cereal': get_object_or_404(Cereal, pk=id)
			})
	else:
		messages.info(request, "You do not have an order.")
		return render(request, 'cereal/cereal_details.html', {
			'cereal': get_object_or_404(Cereal, pk=id)
		})
