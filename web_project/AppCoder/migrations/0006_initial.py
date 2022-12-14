# Generated by Django 4.1.1 on 2022-10-02 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("AppCoder", "0005_delete_collaboration_delete_donation_delete_job"),
    ]

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
                ("bio", models.CharField(max_length=500)),
                ("createdate", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Job",
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
                ("jobrol", models.CharField(max_length=20)),
                ("development", models.BooleanField()),
                ("design", models.BooleanField()),
                ("business", models.BooleanField()),
                ("createdate", models.DateField(null=True)),
                (
                    "donation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppCoder.donation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Collaboration",
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
                ("payment", models.IntegerField()),
                ("createdate", models.DateField(null=True)),
                (
                    "donation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppCoder.donation",
                    ),
                ),
            ],
        ),
    ]
