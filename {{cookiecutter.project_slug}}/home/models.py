from django.db import models

from wagtailmetadata.models import MetadataPageMixin
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import (
    FieldPanel, InlinePanel
)
from wagtailsvg.models import Svg
from wagtailsvg.edit_handlers import SvgChooserPanel

# HOMEPAGE
class HomePage(MetadataPageMixin, Page):
    svgBanner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Imagen SVG 1200x600'
    )
    imgBanner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Procurar imagen webp con dimensiones 1200x600'
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('svgBanner'),
        FieldPanel('imgBanner'),
        
        InlinePanel('quienes_somos', label="Quienes Somos"),
        InlinePanel('a_quienes', label="Tipo de Clientes"),
    ]

    # parent_page_types = []

class NServicios(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='quienes_somos')
    title = models.CharField("Titulo", max_length=20, blank=True)
    description = models.TextField("Contenido", max_length=250, blank=True)
    display = models.BooleanField(default=True)
    svg = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        SvgChooserPanel('svg'),
        FieldPanel('display'),
    ]

class AQuien(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='a_quienes')
    title = models.CharField("Titulo", max_length=20, blank=True)
    display = models.BooleanField(default=True)
    svg = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    panels = [
        FieldPanel('title'),
        SvgChooserPanel('svg'),
        FieldPanel('display'),
    ]

