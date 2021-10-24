# Generated by Django 3.2.7 on 2021-10-16 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lappyng_app', '0017_auto_20211003_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Newsletter Category',
            },
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('conf_num', models.CharField(max_length=30)),
                ('confirmed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('news_letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.newslettercategory')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lappyng_app.products')),
            ],
        ),
    ]