from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ReferenceInfo(models.Model):
    link = models.CharField(verbose_name="Ссылка для конкретного email", max_length=100)
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
