# Generated by Django 4.1.2 on 2023-01-31 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_add_cart_offer_remove_add_cart_our_special_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_cart',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='add_cart',
            name='our_special',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='add_cart',
            name='top_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='temp_cart',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='temp_cart',
            name='our_special',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='temp_cart',
            name='top_add',
            field=models.BooleanField(default=False),
        ),
    ]
