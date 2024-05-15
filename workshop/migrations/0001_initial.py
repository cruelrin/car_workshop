# Generated by Django 5.0.4 on 2024-05-15 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Master",
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
                ("full_name", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("experience", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
                ("photo", models.ImageField(upload_to="service_photos/")),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("client_id", models.IntegerField()),
                ("car_model", models.CharField(max_length=100)),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "master",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workshop.master",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workshop.service",
                    ),
                ),
            ],
        ),
    ]
