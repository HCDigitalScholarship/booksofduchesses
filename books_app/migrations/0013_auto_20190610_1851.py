# Generated by Django 2.2.2 on 2019-06-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0012_auto_20190610_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateowned',
            name='conf_or_possible',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Possible', 'Possible')], default='Confirmed', max_length=9),
        ),
    ]