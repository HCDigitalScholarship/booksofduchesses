# Generated by Django 2.2.2 on 2019-11-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0082_auto_20191030_1708")]

    operations = [
        migrations.CreateModel(
            name="Evidence",
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
                (
                    "conf_or_possible",
                    models.CharField(
                        choices=[("confirmed", "confirmed"), ("possibly", "possibly")],
                        default="confirmed",
                        max_length=9,
                    ),
                ),
                ("evidence", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name="dateowned", options={"ordering": ("book_owner",)}
        ),
    ]
