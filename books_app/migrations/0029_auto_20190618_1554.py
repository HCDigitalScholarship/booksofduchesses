# Generated by Django 2.2.2 on 2019-06-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0028_auto_20190618_1524")]

    operations = [migrations.RemoveField(model_name="book", name="bibliography")]
