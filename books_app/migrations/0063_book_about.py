# Generated by Django 2.2.2 on 2019-07-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0062_book_scribes")]

    operations = [
        migrations.AddField(
            model_name="book", name="about", field=models.TextField(blank=True)
        )
    ]
