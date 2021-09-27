# Generated by Django 3.2.7 on 2021-09-25 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lappyng_app', '0016_remove_products_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('rating', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), ('', 'Choose Rating')], default='', max_length=10)),
                ('review', models.TextField()),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lappyng_app.products')),
            ],
        ),
    ]
