from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel

class AlbumPage(Page):
    album_title = models.TextField()
    album_art = models.ImageField()

    description = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("album_title"),
        FieldPanel("album_art"),
        FieldPanel("description")
    ]