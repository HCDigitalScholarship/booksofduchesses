# Generated by Django 2.2.2 on 2019-07-16 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0050_booklocation_owner_at_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='book',
        ),
    ]