# Generated by Django 3.2.7 on 2021-11-04 06:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lappyng_app', '0017_auto_20211003_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='slide_img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Slide Image'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_img',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='Use this Image dimension 157px X 88px', max_length=255, null=True, verbose_name='Brand Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_img',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='Use this Image dimension 170px X 100px', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_img_banner',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='Use this Image dimension 848px X 132px', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_img_banner2',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='Use this Image dimension 848px X 132px', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homesidebanner',
            name='banner',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hometopbanner',
            name='banner',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hometwosidebanner',
            name='banner',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='image3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
