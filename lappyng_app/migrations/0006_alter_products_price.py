# Generated by Django 3.2.7 on 2021-10-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lappyng_app', '0005_alter_products_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
    ]
