# Generated by Django 2.2.2 on 2019-11-22 17:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0089_book_printer'),
    ]

    operations = [
        migrations.AddField(
            model_name='scribe',
            name='birth_year',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='scribe',
            name='death_year',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='scribe',
            name='gender',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='scribe',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='scribe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='scribe',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Further Information (link)'),
        ),
    ]
