from tabnanny import verbose
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    title = models.CharField(max_length = 255, unique = True)
    image = models.ImageField(upload_to = "categoryImage", blank = True, null = True)
    parent = TreeForeignKey('self', on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    



