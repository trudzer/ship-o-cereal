from django.forms import ModelForm, widgets
from cereal.models import Cereal
from django import forms

class CerealUpdateForm(ModelForm):
    class Meta:
        model = Cereal
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Name' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Description' }),
            'category': widgets.Select(attrs={ 'class': 'form-control', 'placeholder': 'Category' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Price' }),
            'manufacturer': widgets.Select(attrs={ 'class': 'form-control', 'placeholder': 'Manufacturer' }),
            'on_sale': widgets.CheckboxInput(attrs={ 'class': 'checkbox', 'placeholder': 'On Sale' })
        }

class CerealCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Image' }))
    class Meta:
        model = Cereal
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Name' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Description' }),
            'category': widgets.Select(attrs={ 'class': 'form-control', 'placeholder': 'Category' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Price' }),
            'manufacturer': widgets.Select(attrs={ 'class': 'form-control', 'placeholder': 'Manufacturer' }),
            'on_sale': widgets.CheckboxInput(attrs={ 'class': 'checkbox', 'placeholder': 'On sale' })
        }