from rest_framework import serializers

from .models import *

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'parent')