# Generated by Django 3.2.9 on 2023-03-14 15:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_paymentcomplete_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentcomplete',
            name='rating',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]