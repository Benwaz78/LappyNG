# Generated by Django 3.2.7 on 2021-10-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lappyng_app', '0008_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
    ]