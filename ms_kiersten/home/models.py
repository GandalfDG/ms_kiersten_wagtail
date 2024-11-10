from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    headline = RichTextField()
    biography = RichTextField()
    
    updated = models.DateField(auto_now=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('biography')
    ]