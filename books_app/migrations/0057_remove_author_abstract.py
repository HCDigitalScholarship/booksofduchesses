# Generated by Django 2.2.2 on 2019-07-24 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("books_app", "0056_author_link")]

    operations = [migrations.RemoveField(model_name="author", name="abstract")]
