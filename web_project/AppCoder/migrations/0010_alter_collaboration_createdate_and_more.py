# Generated by Django 4.1.1 on 2022-10-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0009_alter_collaboration_createdate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collaboration",
            name="createdate",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="donation",
            name="createdate",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="createdate",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]