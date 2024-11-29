from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel

class AlbumPage(Page):
    album_title = models.TextField()
    album_cover_image = models.ForeignKey("wagtailimages.Image", on_delete=models.SET_NULL,
                                  related_name="+", null=True)

    description = RichTextField()
    album_streaming_link = models.URLField(null=True)

    content_panels = Page.content_panels + [
        FieldPanel("album_title"),
        FieldPanel("album_cover_image"),
        FieldPanel("description"),
        FieldPanel("album_streaming_link")
    ]

class BlogPost(Page):
    post_summary = RichTextField()

    post_cover_image = models.ImageField()

    post_content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("post_cover_image"),
        FieldPanel("post_summary"),
        FieldPanel("post_content")
    ]

class BlogList(Page):
    pass