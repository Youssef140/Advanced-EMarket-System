# Generated by Django 3.1.7 on 2021-04-21 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_offer_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='brands',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]