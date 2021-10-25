# Generated by Django 2.2.2 on 2019-10-25 16:22

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0076_auto_20191025_1621")]

    operations = [
        migrations.CreateModel(
            name="Printer",
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
                ("name", models.CharField(max_length=200)),
                (
                    "link",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        verbose_name="Further Information (link)",
                    ),
                ),
                ("birth_date", models.CharField(blank=True, max_length=200)),
                ("death_date", models.CharField(blank=True, max_length=200)),
                ("gender", models.CharField(blank=True, max_length=200)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="translator",
            name="gender",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="translator",
            name="geom",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, null=True, srid=4326
            ),
        ),
        migrations.AddField(
            model_name="translator",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
