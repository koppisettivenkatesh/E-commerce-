# Generated by Django 4.1.2 on 2022-12-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_top_ads',
            name='link',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
