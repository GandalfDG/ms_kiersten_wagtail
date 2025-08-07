from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
# Create your models here.

class KinderHome(Page):
    headline = models.TextField()
    subheading = models.TextField()

    hero_image = models.ImageField()

    main_content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("headline"),
        FieldPanel("subheading"),
        FieldPanel("hero_image"),
        FieldPanel("main_content")
    ]