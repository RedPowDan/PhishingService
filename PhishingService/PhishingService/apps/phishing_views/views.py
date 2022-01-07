from django.http import HttpRequest
from django.conf import settings

from PhishingService.apps.phishing_views.services import ReferenceInfoService


def index(request: HttpRequest):
    key = getattr(settings, "KEY_FOR_GENERATED_KEY", None)
    generated_link = request.GET.get(key, None)
    reference_info = ReferenceInfoService.get_reference_info_by_generated_link(generated_link)
    if reference_info is not None:
        reference_info.is_read = True
        reference_info.save()


