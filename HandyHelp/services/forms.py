from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'category', 'price', 'location', 'image']
        labels = {
            'title': 'Назва',
            'description': 'Опис',
            'category': 'Категорія',
            'price': 'Ціна',
            'location': 'Місце надання послуги',
            'image': 'Зображення'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назву послуги'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введіть опис послуги'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введіть ціну послуги'}),
            'location': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Введіть місце надання послуги'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Ціна не може бути від'ємною")
        return price
