# Generated by Django 2.2.2 on 2019-06-17 16:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0019_auto_20190612_2009")]

    operations = [
        migrations.CreateModel(
            name="AuthorPlaceDateLived",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place_date_lived", models.CharField(max_length=200, null=True)),
                (
                    "place",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
                ("place_name", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OwnerPlaceDateLived",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place_date_lived", models.CharField(max_length=200, null=True)),
                (
                    "place",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
                ("place_name", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="author",
            name="date_place_lived",
            field=models.ManyToManyField(
                blank=True, to="books_app.AuthorPlaceDateLived"
            ),
        ),
        migrations.AddField(
            model_name="owner",
            name="date_place_lived",
            field=models.ManyToManyField(
                blank=True, to="books_app.OwnerPlaceDateLived"
            ),
        ),
    ]
