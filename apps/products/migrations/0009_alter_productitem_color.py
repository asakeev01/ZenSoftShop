# Generated by Django 4.0.3 on 2022-03-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_categories_alter_product_compound_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='color',
            field=models.CharField(choices=[('BLACK', 'Black'), ('RED', 'Red'), ('ORANGE', 'Orange'), ('BROWN', 'Brown'), ('PURPLE', 'Purple'), ('YELLOW', 'Yellow'), ('BLUE', 'Blue')], max_length=50),
        ),
    ]
