# Generated by Django 2.2.2 on 2020-02-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0097_auto_20200212_2006")]

    operations = [
        migrations.AddField(
            model_name="ownerplacedatelived",
            name="b",
            field=models.CharField(default="Test", editable=False, max_length=7),
        ),
        migrations.AlterField(
            model_name="book",
            name="comments",
            field=models.TextField(blank=True, verbose_name="User Suggestion Comments"),
        ),
    ]
