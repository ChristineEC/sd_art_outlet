# Generated by Django 4.2 on 2025-03-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artworks", "0009_alter_artwork_artist"),
    ]

    operations = [
        migrations.AddField(
            model_name="artist",
            name="mini_bio",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
