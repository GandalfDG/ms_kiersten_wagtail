from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from modelcluster.fields import ParentalKey
from wagtail.models import Orderable


class HomePage(Page):
    headline = RichTextField()
    biography = RichTextField()
    
    updated = models.DateField(auto_now=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        InlinePanel('home_menu_links', heading='Menu Links', label='link'),
        FieldPanel('biography'),
    ]

class HomePageMenuLink(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='home_menu_links')
    
    name = models.TextField()
    url = models.URLField()

    boxicons_icon_name = models.TextField()