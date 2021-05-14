from django.forms import ModelForm, widgets
from cart.models import BillingAddress

class BillingAddressForm(ModelForm):
    class Meta:
        model = BillingAddress
        exclude = [ 'id', 'user' ]
        widgets = {
            "full_name": widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Full name' }),
            "street_name": widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Street name' }),
            "house_number": widgets.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'House number' }),
            "city": widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'City' }),
            "country": widgets.Select(attrs={ 'class': 'form-control', 'placeholder': 'Country' }),
            "postal_code": widgets.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Postal code' })
        }