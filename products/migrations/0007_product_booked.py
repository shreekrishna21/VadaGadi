# Generated by Django 3.2.9 on 2023-01-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_booking_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='booked',
            field=models.BooleanField(default=False, null=True),
        ),
    ]