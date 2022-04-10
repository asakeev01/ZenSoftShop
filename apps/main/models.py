from django.db import models


class Slider(models.Model):
    pass


class SliderImage(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='slider_images')
    image = models.ImageField(upload_to='sliderImage')


class Advantage(models.Model):
    image = models.ImageField(upload_to='advantageImage')
    header = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
