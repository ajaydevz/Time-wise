# Generated by Django 4.2.6 on 2023-11-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=50, unique=True)),
                ("category_image", models.ImageField(upload_to="photos/categories/")),
                ("description", models.TextField(blank=True, max_length=225)),
                ("is_activate", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
    ]
