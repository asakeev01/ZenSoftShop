# Generated by Django 4.0.3 on 2022-03-31 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_productitem_color_productitem_color_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productitem',
            old_name='color',
            new_name='colors',
        ),
    ]
