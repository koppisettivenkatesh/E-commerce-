# Generated by Django 4.1.2 on 2023-02-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_wishlist_order_id_remove_wishlist_payment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.CharField(default='none', max_length=1000),
        ),
    ]