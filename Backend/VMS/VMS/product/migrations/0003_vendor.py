# Generated by Django 5.0.2 on 2024-03-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendor",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=15)),
                ("is_deleted", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
