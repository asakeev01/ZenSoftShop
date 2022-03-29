# Generated by Django 4.0.3 on 2022-03-28 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='compound',
            field=models.CharField(default='cotton', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productitem',
            name='material',
            field=models.CharField(default='cotton', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productitem',
            name='new',
            field=models.BooleanField(default=True),
        ),
    ]
