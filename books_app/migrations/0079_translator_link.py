# Generated by Django 2.2.2 on 2019-10-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0078_remove_translator_arlima")]

    operations = [
        migrations.AddField(
            model_name="translator",
            name="link",
            field=models.CharField(blank=True, max_length=200, null=True),
        )
    ]
