# Generated by Django 4.1.1 on 2022-10-02 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0004_rename_collaboration_collaboration_payment"),
    ]

    operations = [
        migrations.DeleteModel(name="Collaboration",),
        migrations.DeleteModel(name="Donation",),
        migrations.DeleteModel(name="Job",),
    ]
