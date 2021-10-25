# Generated by Django 2.2.2 on 2019-10-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0079_translator_link")]

    operations = [
        migrations.AlterField(
            model_name="dateowned",
            name="conf_or_possible",
            field=models.CharField(
                choices=[("Confirmed", "Confirmed"), ("Possibly", "Possibly")],
                default="Confirmed",
                max_length=9,
            ),
        )
    ]
