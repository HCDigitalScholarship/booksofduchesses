# Generated by Django 2.2.2 on 2019-06-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0025_auto_20190617_2022")]

    operations = [
        migrations.RemoveField(model_name="author", name="about"),
        migrations.AddField(
            model_name="author",
            name="abstract",
            field=models.TextField(blank=True, verbose_name="About"),
        ),
    ]
