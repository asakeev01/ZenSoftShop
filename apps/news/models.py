from django.db import models

from ckeditor.fields import RichTextField


class News(models.Model):
    image = models.ImageField(upload_to='newsImage')
    header = models.CharField(max_length=55)
    description = RichTextField()

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
