from .models import Room
from django import forms

class RoomSearchForm(forms.Form):
    room_type = forms.CharField(
        required=False,
        label='Тип комнаты',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тип комнаты'})
    )
    min_price = forms.DecimalField(
        required=False,
        label='Минимальная цена',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите минимальную цену'})
    )
    max_price = forms.DecimalField(
        required=False,
        label='Максимальная цена',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите максимальную цену'})
    )
    is_available = forms.BooleanField(
        required=False,
        label='Только доступные комнаты',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'price', 'is_available']
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'room_type': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
