# Generated by Django 3.2.7 on 2021-11-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lappyng_app', '0020_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='slug',
            field=models.SlugField(default='frequently-asked-questions', unique=True),
            preserve_default=False,
        ),
    ]
