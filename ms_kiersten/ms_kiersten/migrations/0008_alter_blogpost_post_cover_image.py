# Generated by Django 5.1.3 on 2024-12-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ms_kiersten", "0007_bloglist_blog_headline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="post_cover_image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
