from django import forms

from .models import *

from django.core.exceptions import ValidationError


class BasketItemCreateForm(forms.ModelForm):

    class Meta:
        model = BasketItem
        fields = ['basket', 'product_item', 'size', 'quantity']

    def clean(self):
        size = self.cleaned_data.get('size')
        object_size = Size.objects.get(id=size)
        if self.cleaned_data.get('quantity') > object_size.quantity:
            raise ValidationError("Not enough quantity")
        else:
            return self.cleaned_data