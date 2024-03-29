# Generated by Django 2.2.2 on 2020-06-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books_app", "0099_remove_ownerplacedatelived_b")]

    operations = [
        migrations.AddField(
            model_name="owner",
            name="bio",
            field=models.URLField(blank=True, max_length=500, null=True),
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
                    ("Son-in-law", "Son-in-Law"),
                    ("Mother-in-law", "Mother-in-law"),
                    ("Father-in-law", "Father-in-law"),
                    ("Sister-in-law", "Sister-in-law"),
                    ("Brother-in-law", "Brother-in-law"),
                    ("God-son", "God-son"),
                    ("God-parent", "God-parent"),
                    ("God-parent", "God-parent"),
                    ("God-Daughter", "God-Daughter"),
                    ("Niece", "Niece"),
                    ("Nephew", "Nephew"),
                    ("Grandmother", "Grandmother"),
                    ("Grandfather", "Grandafather"),
                    ("Great Aunt", "Great Aunt"),
                    ("Great Uncle", "Great Uncle"),
                    ("Granddaughter", "Granddaughter"),
                    ("Grandson", "Grandson"),
                    ("Grand Niece", "Grand Niece"),
                    ("Grand Nephew", "Grand Nephew"),
                    ("Other", "Other"),
                ],
                default="Father",
                max_length=40,
            ),
        ),
    ]
