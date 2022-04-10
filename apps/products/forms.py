from django import forms

from .models import *

class ProductItemForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = ['product', 'colors']

    def clean(self):
        colors = self.cleaned_data.get('colors')
        if not colors:
            return self.cleaned_data
        product = self.cleaned_data.get('product')
        product_items = ProductItem.objects.filter(product=product)
        colors_dict = {}
        for color in colors:
            colors_dict[color] = 1
        for item in product_items:
            item_colors_dict = {}
            item_colors = Color.objects.filter(product_item=item)
            for item_color in item_colors:
                item_colors_dict[item_color] = 1
            if colors_dict == item_colors_dict:
                raise ValidationError("These colors already exist")
        return self.cleaned_data



