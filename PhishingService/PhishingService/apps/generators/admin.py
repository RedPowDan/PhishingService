from django.contrib import admin
from .models import *
# Register your models here.


class ReferenceInfoTable(admin.ModelAdmin):
    readonly_fields = ("link", "is_read", "is_post_data", "count_views")


admin.site.register(ReferenceInfo, ReferenceInfoTable)
