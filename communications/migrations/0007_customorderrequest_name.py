# Generated by Django 4.2 on 2025-04-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("communications", "0006_customorderrequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="customorderrequest",
            name="name",
            field=models.CharField(default="", max_length=255),
        ),
    ]
