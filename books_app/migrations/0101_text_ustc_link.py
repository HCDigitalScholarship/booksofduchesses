# Generated by Django 2.2.2 on 2020-06-22 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0100_auto_20200619_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='ustc_link',
            field=models.CharField(blank=True, max_length=800, verbose_name='USTC Link'),
        ),
    ]
