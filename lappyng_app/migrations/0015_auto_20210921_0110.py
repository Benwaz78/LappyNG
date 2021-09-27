# Generated by Django 3.2.7 on 2021-09-21 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lappyng_app', '0014_auto_20210921_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='best_seller',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='hot_deal',
            field=models.BooleanField(blank=True, null=True, verbose_name='Hot Deals of this Week'),
        ),
        migrations.DeleteModel(
            name='Tab',
        ),
    ]
