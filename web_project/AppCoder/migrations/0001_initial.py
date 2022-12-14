# Generated by Django 4.1.1 on 2022-10-02 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Donation",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("dateofbirht", models.DateField()),
                ("collaboration", models.IntegerField()),
                ("bio", models.CharField(max_length=500)),
                ("JobRol", models.CharField(max_length=20)),
                ("development", models.BooleanField()),
                ("design", models.BooleanField()),
                ("business", models.BooleanField()),
            ],
        ),
    ]
