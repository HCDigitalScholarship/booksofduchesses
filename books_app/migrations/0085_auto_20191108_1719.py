# Generated by Django 2.2.2 on 2019-11-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0084_dateowned_ownership_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateowned',
            name='ownership_type',
            field=models.ManyToManyField(to='books_app.Evidence'),
        ),
        migrations.AlterField(
            model_name='evidence',
            name='conf_or_possible',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Possible', 'Possible')], default='confirmed', max_length=9),
        ),
    ]
