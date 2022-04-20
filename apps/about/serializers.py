from rest_framework import serializers

from .models import *


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ('image1', 'image2', 'image3', 'header', 'description')