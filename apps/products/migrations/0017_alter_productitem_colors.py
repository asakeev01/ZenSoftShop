# Generated by Django 4.0.3 on 2022-04-04 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_rename_color_productitem_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='colors',
            field=models.ManyToManyField(related_name='product_item', to='products.color'),
        ),
    ]
