# Generated by Django 4.2.7 on 2024-02-28 00:56

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("ads", "0004_fav_ad_favorites"),
    ]

    operations = [
        migrations.AddField(
            model_name="ad",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
