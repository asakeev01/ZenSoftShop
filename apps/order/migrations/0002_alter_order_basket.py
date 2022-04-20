# Generated by Django 4.0.3 on 2022-04-18 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_alter_basketitem_basket_alter_basketitem_quantity'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='basket.basket'),
        ),
    ]