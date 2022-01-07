from django.contrib import admin

# Register your models here.
from django.shortcuts import render
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import ViewModel


class ViewModelTable(admin.ModelAdmin):
    list_display = ("link_official_site",)


admin.site.register(ViewModel, ViewModelTable)
