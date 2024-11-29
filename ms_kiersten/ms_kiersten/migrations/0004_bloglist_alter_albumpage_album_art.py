# Generated by Django 5.1.3 on 2024-11-29 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ms_kiersten", "0003_remove_blogpost_post_published_date"),
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogList",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.AlterField(
            model_name="albumpage",
            name="album_art",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
    ]