# Generated by Django 2.2.2 on 2019-07-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0063_book_about")]

    operations = [
        migrations.RemoveField(model_name="author", name="date_place_lived"),
        migrations.RemoveField(model_name="book", name="library"),
        migrations.RemoveField(model_name="book", name="owner"),
        migrations.RemoveField(model_name="bookslanguage", name="geom"),
        migrations.RemoveField(model_name="tag", name="geom"),
        migrations.AlterField(
            model_name="book",
            name="about",
            field=models.TextField(blank=True, verbose_name="About/Content"),
        ),
        migrations.AlterField(
            model_name="owner",
            name="book_date",
            field=models.ManyToManyField(
                blank=True,
                to="books_app.DateOwned",
                verbose_name="Instance of Book Ownership",
            ),
        ),
        migrations.AlterField(
            model_name="relative",
            name="relation",
            field=models.CharField(
                choices=[
                    ("Father", "Father"),
                    ("Mother", "Mother"),
                    ("Spouse", "Spouse"),
                    ("Son", "Son"),
                    ("Daughter", "Daughter"),
                    ("Brother", "Brother"),
                    ("Sister", "Sister"),
                    ("Aunt", "Aunt"),
                    ("Uncle", "Uncle"),
                    ("Cousin", "Cousin"),
                    ("Daughter-in-law", "Daughter-in-law"),
                    ("Sister-in-law", "Son-in-Law"),
                    ("Mother-in-law", "Mother-in-law"),
                    ("Father-in-law", "Father-in-law"),
                    ("Sister-in-law", "Sister-in-law"),
                    ("Brother-in-law", "Brother-in-law"),
                    ("God-son", "God-son"),
                    ("God-parent", "God-parent"),
                    ("God-parent", "God-parent"),
                    ("God-Daughter", "God-Daughter"),
                    ("Other", "Other"),
                ],
                default="Father",
                max_length=40,
            ),
        ),
        migrations.DeleteModel(name="AuthorPlaceDateLived"),
    ]
