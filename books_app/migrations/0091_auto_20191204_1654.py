# Generated by Django 2.2.2 on 2019-12-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0090_auto_20191122_1734")]

    operations = [
        migrations.AddField(
            model_name="owner",
            name="arms",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="owner",
            name="signatures",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="author",
            name="gender",
            field=models.CharField(
                choices=[("Female", "Female"), ("Male", "Male")],
                default="Female",
                max_length=9,
            ),
        ),
        migrations.AlterField(
            model_name="illuminator",
            name="gender",
            field=models.CharField(
                choices=[("Female", "Female"), ("Male", "Male")],
                default="Female",
                max_length=9,
            ),
        ),
        migrations.AlterField(
            model_name="printer",
            name="gender",
            field=models.CharField(
                choices=[("Female", "Female"), ("Male", "Male")],
                default="Female",
                max_length=9,
            ),
        ),
        migrations.AlterField(
            model_name="scribe",
            name="gender",
            field=models.CharField(
                choices=[("Female", "Female"), ("Male", "Male")],
                default="Female",
                max_length=9,
            ),
        ),
        migrations.AlterField(
            model_name="translator",
            name="gender",
            field=models.CharField(
                choices=[("Female", "Female"), ("Male", "Male")],
                default="Female",
                max_length=9,
            ),
        ),
    ]
