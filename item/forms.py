from django import forms
from .models import *


class AddItems(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'quantity', 'image', 'available', 'expiration_date']

class ExcelUploadForm(forms.Form):
    file = forms.FileField()

