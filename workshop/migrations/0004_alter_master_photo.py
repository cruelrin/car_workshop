# Generated by Django 5.0.4 on 2024-05-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshop", "0003_master_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="master",
            name="photo",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
