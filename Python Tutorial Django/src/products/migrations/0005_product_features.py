# Generated by Django 3.1.2 on 2021-03-23 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210322_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='features',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
