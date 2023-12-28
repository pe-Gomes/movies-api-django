# Generated by Django 5.0 on 2023-12-27 19:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watch_list", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StreamingPlatform",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=255)),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="WatchList",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=255)),
                ("release_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Movie",
        ),
    ]