# Generated by Django 2.2.2 on 2019-10-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0071_auto_20191002_1636")]

    operations = [
        migrations.AddField(
            model_name="book",
            name="printer",
            field=models.CharField(
                blank=True, max_length=200, verbose_name="Printer Information"
            ),
        )
    ]
