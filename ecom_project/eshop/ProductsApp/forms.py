# forms.py
from django import forms
from .models import Review
from django.db import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']  # Ajoutez d'autres champs au besoin




class PriceRangeForm(forms.Form):
    min_price = forms.DecimalField(required=False, min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Min Price'}))
    max_price = forms.DecimalField(required=False, min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Max Price'}))


from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['email', 'address', 'mobile', 'status']
