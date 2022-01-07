from typing import Optional

from django.contrib.auth.models import User
from django.shortcuts import render

from PhishingService.apps.generators.models import ReferenceInfo


class ReferenceInfoService:
    @staticmethod
    def get_user_by_generated_link(generated_link) -> Optional[User, None]:
        exist_reference_info = ReferenceInfoService.get_reference_info_by_generated_link(generated_link)
        if exist_reference_info is None:
            return None
        return exist_reference_info.user

    @staticmethod
    def get_reference_info_by_generated_link(generated_link: str) -> ReferenceInfo:
        if generated_link is None:
            return None

        try:
            exist_reference_info = ReferenceInfo.objects.get(link=generated_link)

            if exist_reference_info.user is not None:
                return None
        except:
            return None

        return exist_reference_info

    @staticmethod
    def get_view_by_reference_info(reference_info: ReferenceInfo):
        return None