# Generated by Django 5.1.3 on 2024-11-10 13:59

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_homepage_headline_homepage_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="biography",
            field=wagtail.fields.RichTextField(
                default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et dapibus nisl, vestibulum fringilla lacus. Cras facilisis nulla id tempor cursus. Aenean eget massa neque. Vestibulum tincidunt ultrices turpis in malesuada. Maecenas et tortor tortor. Nullam ac ex non augue hendrerit lacinia cursus id quam. Integer tellus tortor, interdum at mauris nec, feugiat aliquet neque. Donec pharetra elementum ligula, non luctus eros placerat nec. Nulla facilisi."
            ),
            preserve_default=False,
        ),
    ]
