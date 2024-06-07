from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username', 'phone')

class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username', 'phone')

class SellerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username', 'phone')
