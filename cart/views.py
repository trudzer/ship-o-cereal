from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import View

from cart.forms.checkout_form import BillingAddressForm
from cart.models import OrderItem, Order, BillingAddress, Payment
from cereal.models import Cereal
from django.contrib import messages

import stripe

stripe.api_key = "sk_test_51IqzhLEi4iZpiAj5QZyEHs9jp44UUAbgHrq11LWjk7Zzc26RWeKK7cDdoXMMoLFDPoWpxCJ0ttK98ONDTbuetkS600eKWoBHnD"


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


class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = BillingAddressForm()
            context = {
                'form': form
            }
            return render(self.request, 'cart/checkout.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("/")

    def post(self, *args, **kwargs):
        form = BillingAddressForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            billing_address = BillingAddress.objects.get(user=self.request.user)
            if form.is_valid():
                full_name = form.cleaned_data.get('full_name')
                street_name = form.cleaned_data.get('street_name')
                house_number = form.cleaned_data.get('house_number')
                city = form.cleaned_data.get('city')
                country = form.cleaned_data.get('country')
                postal_code = form.cleaned_data.get('postal_code')
                billing_address.delete()
                billing_address = BillingAddress(
                    user=self.request.user,
                    full_name=full_name,
                    street_name=street_name,
                    house_number=house_number,
                    city=city,
                    country=country,
                    postal_code=postal_code
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                return redirect('/cart/payment')
            messages.warning(self.request, "Failed checkout")
            return redirect('/cart/checkout')
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")


def checkout_view(request):
    if request.method == 'POST':
        form = BillingAddressForm(data=request.POST)
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            if form.is_valid():
                billing_address = form.save(commit=False)
                billing_address.user = request.user
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                return redirect('/cart/payment.html')
            messages.warning(request, "Failed checkout")
            return redirect('/cart/checkout')
        except ObjectDoesNotExist:
            messages.error(request, "You do not have an active order")
            return redirect("/cart/checkout")

    else:
        form = BillingAddressForm()
    return render(request, 'cart/checkout.html', {
        'form': form
    })


class PaymentView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            return render(self.request, "cart/payment.html")
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        token = self.request.POST.get('stripeToken')
        amount = int(order.get_total() * 100)

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                source=token
            )

            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.user = self.request.user
            payment.amount = order.get_total()
            payment.save()

            order.ordered = True
            order.payment = payment
            order.save()

            return render(self.request, "cart/confirmation.html")

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            messages.error(self.request, f"{err.get('message')}")
            return redirect("/")

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.error(self.request, "Rate limited error")
            return redirect("/")

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            messages.error(self.request, "Invalid parameters")
            return redirect("/")

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            messages.error(self.request, "Not authenticated")
            return redirect("/")

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.error(self.request, "Network error")
            return redirect("/")

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.error(self.request, "Something went wrong, you were not charged. Please try again.")
            return redirect("/")

        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            messages.error(self.request, "A serious error. We have been notified.")
            return redirect("/")

def confirmation(request):
    return render(request, 'cart/confirmation.html')