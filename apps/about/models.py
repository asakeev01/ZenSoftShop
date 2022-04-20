from django.db import models

from ckeditor.fields import RichTextField


class About(models.Model):
    image1 = models.ImageField(upload_to='aboutImage')
    image2 = models.ImageField(upload_to='aboutImage')
    image3 = models.ImageField(upload_to='aboutImage')
    header = models.CharField(max_length=55)
    description = RichTextField()

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'