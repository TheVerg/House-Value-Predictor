from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PricePredictionForm(forms.Form):
    bedrooms = forms.IntegerField(label='Bedrooms', min_value=0)
    price = forms.IntegerField(label='Price', min_value=0)
    area_sqm = forms.IntegerField(label='Area Sqm', min_value=0)
    malls   = forms.IntegerField(label='malls', max_value=5)
    location = forms.IntegerField(label='Location',min_value=0, max_value=1)

class UserRegisterForm(UserCreationForm):
    pass