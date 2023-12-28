# Generated by Django 5.0 on 2023-12-28 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watch_list", "0002_streamingplatform_watchlist_delete_movie"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="platform",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watch_list",
                to="watch_list.streamingplatform",
            ),
            preserve_default=False,
        ),
    ]
