# Generated by Django 3.1.7 on 2021-05-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    # dependencies = [
    #     ('listings', '0014_offer_brands'),
    # ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_offer',
            field=models.BooleanField(default=False),
        ),
    ]