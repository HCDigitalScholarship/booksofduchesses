# Generated by Django 2.2.2 on 2019-06-10 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("books_app", "0004_auto_20190610_1444")]

    operations = [
        migrations.RenameField(
            model_name="text", old_name="name_eng", new_name="english_name"
        )
    ]
