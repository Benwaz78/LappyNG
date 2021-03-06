# Generated by Django 3.2.7 on 2021-10-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lappyng_app', '0012_hometopbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeTwoSideBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner1', models.ImageField(upload_to='uploads/')),
                ('link1', models.URLField(blank=True, null=True)),
                ('banner2', models.ImageField(upload_to='uploads/')),
                ('link2', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Home Two SideBanner',
            },
        ),
    ]
