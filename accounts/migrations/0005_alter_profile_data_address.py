# Generated by Django 4.1.2 on 2023-01-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_data_default_shipping_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_data',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]