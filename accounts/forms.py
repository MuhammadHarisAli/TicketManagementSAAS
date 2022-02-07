from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')

class ProfileForm(forms.Form):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    name = forms.CharField(
        label='Name',
        max_length=255,
        required=True
    )
    email = forms.EmailField(
        label='email',
        max_length=255,
        required=True
    )
    address = forms.CharField(
        label='address',
        max_length=500,
        required=True
    )
    password = forms.CharField(
        label='password',
        max_length=500,
        required=True
    )
    telephone_number = forms.CharField(
        validators=[phone_regex],
        max_length=15,
        label='Cell Phone Number',
        required=True
    )
    image = forms.ImageField(required=False)
