# Generated by Django 3.1.2 on 2021-03-23 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
