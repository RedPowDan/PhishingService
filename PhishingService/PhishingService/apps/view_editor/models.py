from django.db import models

# Create your models here.
from PhishingService.apps.base import BaseModel


class ViewModel(BaseModel):
    link_official_site = models.CharField(verbose_name="Ссылка на официальный сайт",
                                          blank=True,
                                          default="",
                                          max_length=100)
    html_code = models.TextField(verbose_name="html код", default="")

