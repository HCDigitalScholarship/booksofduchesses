# Generated by Django 2.2.2 on 2019-07-25 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0058_auto_20190725_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='illuminators',
        ),
    ]