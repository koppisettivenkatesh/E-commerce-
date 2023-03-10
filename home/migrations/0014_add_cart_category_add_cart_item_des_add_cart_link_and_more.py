# Generated by Django 4.1.2 on 2022-12-13 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_add_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_cart',
            name='category',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_cart',
            name='item_des',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_cart',
            name='link',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_cart',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='add_cart',
            name='item_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='add_cart',
            name='quantity',
            field=models.IntegerField(default='1'),
        ),
    ]
