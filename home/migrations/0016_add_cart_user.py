# Generated by Django 4.1.2 on 2022-12-15 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_delete_home_top_ads_delete_our_special_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_cart',
            name='user',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
