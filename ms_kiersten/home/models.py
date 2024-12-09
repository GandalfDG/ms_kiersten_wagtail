from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel

from modelcluster.fields import ParentalKey
from wagtail.models import Orderable


class HomePage(Page):
    headline = RichTextField()
    biography = RichTextField()
    
    updated = models.DateField(auto_now=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('biography'),
        InlinePanel('photo_gallery', heading='Photo Gallery', label='photo'),
        InlinePanel('home_menu_links', heading='Menu Links', label='link', classname="collapsed"),
    ]

class HomePageMenuLink(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='home_menu_links')
    
    name = models.TextField()
    boxicons_icon_name = models.TextField()
    
    # The link can either be to an external URL
    external_url = models.TextField(null=True, blank=True)
    # or to an internal page
    page_link = models.ForeignKey("wagtailcore.Page", null=True, blank=True, on_delete=models.CASCADE)

    external_url_panel = FieldPanel('external_url')
    internal_page_panel = FieldPanel('page_link')

    panels = [
        FieldPanel('name'),
        FieldPanel('boxicons_icon_name'),
        FieldRowPanel((external_url_panel, internal_page_panel))
    ]

class PhotoGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="photo_gallery")

    photo = models.ForeignKey("wagtailimages.Image", on_delete=models.PROTECT,
                              related_name="+")
    
    caption = RichTextField(null=True, blank=True)

    panels = [
        FieldPanel('photo'),
        FieldPanel('caption'),
    ]
