from django.forms import ModelForm, widgets
from contact_form.models import ContactUs

class ContactUsForm(ModelForm):
    class Meta:
        exclude = ['id']
        model = ContactUs
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Full name' }),
            'email': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Email' }),
            'message': widgets.TextInput(attrs={'class': 'form-control message', 'placeholder': 'Message' })
        }