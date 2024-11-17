# Generated by Django 5.1.3 on 2024-11-17 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_remove_homepagemenulink_url_and_more"),
        ("wagtailcore", "0094_alter_page_locale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepagemenulink",
            name="external_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="homepagemenulink",
            name="page_link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wagtailcore.page",
            ),
        ),
    ]