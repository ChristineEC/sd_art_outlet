# Generated by Django 4.2 on 2025-04-03 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("artworks", "0014_artwork_custom_orderer"),
        ("communications", "0005_alter_contactus_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomOrderRequest",
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
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField(blank=True, null=True)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("have_read", models.BooleanField(default=False)),
                ("replied_to_on", models.DateTimeField(blank=True, null=True)),
                ("artwork_ordered", models.BooleanField(default=False)),
                (
                    "artwork",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="artworks.artwork",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
