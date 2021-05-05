from django.forms import ModelForm, widgets
from contact_form.models import ContactUs

class ContactUsForm(ModelForm):
    class Meta:
        exclude = ['id']
        model = ContactUs
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'email': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'message': widgets.TextInput(attrs={'class': 'form-control message'})
        }