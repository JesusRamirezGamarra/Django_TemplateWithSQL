# Generated by Django 4.1.1 on 2022-10-02 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0003_rename_jobrol_job_jobrol"),
    ]

    operations = [
        migrations.RenameField(
            model_name="collaboration", old_name="collaboration", new_name="payment",
        ),
    ]
