# Generated by Django 3.2.7 on 2021-10-03 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lappyng_app', '0016_auto_20211003_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hometopbanner',
            old_name='banner1',
            new_name='banner',
        ),
        migrations.RenameField(
            model_name='hometopbanner',
            old_name='link1',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='hometopbanner',
            name='banner2',
        ),
        migrations.RemoveField(
            model_name='hometopbanner',
            name='link2',
        ),
    ]
