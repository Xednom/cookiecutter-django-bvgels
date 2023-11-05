# Generated by Django 3.2.8 on 2023-05-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tagging",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("description", models.TextField(blank=True)),
                ("notes", models.TextField(blank=True)),
                ("additional_info", models.TextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
