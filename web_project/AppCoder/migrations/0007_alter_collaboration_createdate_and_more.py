# Generated by Django 4.1.1 on 2022-10-02 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0006_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collaboration",
            name="createdate",
            field=models.DateField(default=datetime.date(2022, 10, 2)),
        ),
        migrations.AlterField(
            model_name="donation",
            name="createdate",
            field=models.DateField(default=datetime.date(2022, 10, 2)),
        ),
        migrations.AlterField(
            model_name="job",
            name="createdate",
            field=models.DateField(default=datetime.date(2022, 10, 2)),
        ),
    ]
