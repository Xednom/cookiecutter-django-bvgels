# Generated by Django 3.2.8 on 2023-05-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0005_alter_client_hourly_rate_currency"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="sub_category",
            field=models.CharField(
                choices=[("n_a", "N/A"), ("regular", "Regular"), ("ftm", "FTM")],
                default="n_a",
                max_length=50,
            ),
        ),
    ]
