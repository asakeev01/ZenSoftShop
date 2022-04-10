from .models import Advantage

from django import forms
from django_svg_image_form_field import SvgAndImageFormField


class AdvantageForm(forms.ModelForm):

    class Meta:
        model = Advantage
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }


