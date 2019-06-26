# Generated by Django 2.2.2 on 2019-06-20 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0029_auto_20190618_1554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bibliography',
            options={'verbose_name_plural': 'Bibliographies'},
        ),
        migrations.AlterModelOptions(
            name='dateowned',
            options={'verbose_name': 'Date owned', 'verbose_name_plural': 'Dates Book Owned'},
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]