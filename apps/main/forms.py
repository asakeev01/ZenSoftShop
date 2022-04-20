from .models import Advantage, Header

from django import forms
from django_svg_image_form_field import SvgAndImageFormField


class AdvantageForm(forms.ModelForm):

    class Meta:
        model = Advantage
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }


class HeaderForm(forms.ModelForm):

    class Meta:
        model = Header
        exclude = []
        field_classes = {
            'logo': SvgAndImageFormField,
        }


