from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    """
    Extended Signup form
    """
    first_name = forms.CharField(max_length=30, label="Ім'я")
    last_name = forms.CharField(max_length=30, label="Прізвище")
