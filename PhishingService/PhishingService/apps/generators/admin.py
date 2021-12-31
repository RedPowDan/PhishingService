from django.contrib import admin
from .models import *
# Register your models here.


class ReferenceInfoTable(admin.ModelAdmin):
    readonly_fields = ("link",)


admin.site.register(ReferenceInfo, ReferenceInfoTable)
