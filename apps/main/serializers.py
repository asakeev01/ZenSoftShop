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


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ('question', 'answer')


class FAQImageSerializer(serializers.ModelSerializer):
    faq = FAQSerializer(many=True)

    class Meta:
        model = FAQImage
        fields = ('image', 'faq')


class FooterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Footer
        fields = ('text', 'type', 'link')


class HeaderSerializer(serializers.ModelSerializer):
    footer = FooterSerializer(many=True)

    class Meta:
        model = Header
        fields = ('footer', 'phone_num', 'logo', 'text')


class PublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Public
        fields = ('header', 'description')


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ('whatsapp', 'telegram')


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ('name', 'number', 'back_call')


