# Generated by Django 4.1.2 on 2022-12-13 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_items_category_alter_home_top_ads_item_des_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image')),
                ('item_name', models.CharField(max_length=1000)),
                ('item_price', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
