# Generated by Django 3.1.7 on 2021-04-11 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20210407_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]