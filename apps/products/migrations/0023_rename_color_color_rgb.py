# Generated by Django 4.0.3 on 2022-04-20 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_remove_color_name_color_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color',
            new_name='rgb',
        ),
    ]
