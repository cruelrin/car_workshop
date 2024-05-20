# Generated by Django 5.0.4 on 2024-05-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="master",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="service",
            name="photo",
            field=models.ImageField(upload_to="images/"),
        ),
    ]