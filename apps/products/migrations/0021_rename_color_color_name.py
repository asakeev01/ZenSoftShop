# Generated by Django 4.0.3 on 2022-04-18 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_color_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color',
            new_name='name',
        ),
    ]