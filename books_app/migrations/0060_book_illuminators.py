# Generated by Django 2.2.2 on 2019-07-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0059_remove_book_illuminators'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='illuminators',
            field=models.ManyToManyField(blank=True, to='books_app.Illuminator'),
        ),
    ]
