# Generated by Django 2.2.2 on 2019-07-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0060_book_illuminators'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='scribes',
        ),
    ]
