# Generated by Django 4.0.3 on 2022-03-23 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=10, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('color', models.CharField(choices=[('BLACK', 'Black'), ('RED', 'Red'), ('ORANGE', 'Orange'), ('BROWN', 'Brown'), ('PURPLE', 'Purple'), ('YELLOW', 'Yellow'), ('BLUE', 'Blue')], max_length=50, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('productItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productitem')),
            ],
        ),
        migrations.CreateModel(
            name='ProductItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('productItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productitem')),
            ],
        ),
    ]
