# Generated by Django 2.2.2 on 2019-07-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0055_auto_20190724_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='link',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
