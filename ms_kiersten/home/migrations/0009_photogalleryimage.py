# Generated by Django 5.1.3 on 2024-12-09 02:47

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_alter_homepagemenulink_external_url"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhotoGalleryImage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("caption", wagtail.fields.RichTextField(null=True)),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photo_gallery",
                        to="home.homepage",
                    ),
                ),
                (
                    "photo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]