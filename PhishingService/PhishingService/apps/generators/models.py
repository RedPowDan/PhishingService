from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from PhishingService.apps.generators.services import GeneratorLink


class ReferenceInfo(models.Model):
    link = models.CharField(verbose_name="Ссылка для конкретного email", max_length=100)
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    is_read = models.BooleanField(verbose_name="Прочитано", default=False)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Ссылка для пользователя'
        verbose_name_plural = 'Ссылки для пользователей'


@receiver(post_save, sender=ReferenceInfo)
def save_user_profile(sender, instance: ReferenceInfo, **kwargs):
    email = str(instance.user.email)
    if email and not instance.link:
        generated_link = GeneratorLink.GetGenerateLinkForEmail(email)
        instance.link = generated_link
        instance.save()


