# apps/hotels/forms.py
from django import forms

class HotelSearchForm(forms.Form):
    name = forms.CharField(required=False, label="Название отеля")
    location = forms.CharField(required=False, label="Местоположение")
    min_rating = forms.DecimalField(required=False, label="Минимальный рейтинг", max_digits=3, decimal_places=2)
