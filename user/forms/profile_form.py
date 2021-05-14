from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'id', 'user' ]
        widgets = {
            'first_name': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'First name' }),
            'last_name': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Last name' }),
            'email': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Email' }),
            'profile_image': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Profile image' })
        }