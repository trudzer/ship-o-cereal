from django.urls import path
from . import views
from .views import Cart_View, PaymentView, CheckoutView

urlpatterns = [
    path('', Cart_View.as_view(), name="cart-index"),
    path('add_to_cart/<int:id>', views.add_to_cart, name="add_to_cart"),
    path('add_to_cart_in_cart/<int:id>', views.add_to_cart_in_cart, name="add_to_cart_in_cart"),
    path('remove_single_item_from_cart/<int:id>', views.remove_single_item_from_cart, name="remove_single_item_from_cart"),
    path('clear_cart/<int:id>', views.clear_cart, name="clear_cart"),
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('payment/', PaymentView.as_view(), name="payment"),
    path('confirmation/', views.confirmation, name="confirmation")
]