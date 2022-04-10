from rest_framework import serializers

from .models import *


class SliderImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SliderImage
        fields = ('image',)


class SliderSerializer(serializers.ModelSerializer):
    slider_images = SliderImageSerializer(many=True)

    class Meta:
        model = Slider
        fields = ('slider_images',)


class AdvantageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advantage
        fields = ('image', 'header', 'description')