import binascii
import os

from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token


class Application(models.Model):
    """ Приложения """
    key = models.CharField(_('Key'), max_length=40, editable=False)
    name = models.CharField(_('Name'), max_length=256)
    created = models.DateTimeField(_('Created'), auto_now_add=True, editable=False)
    custom_data = models.TextField(_('Custom data'), blank=True)

    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def refresh(self):
        """ Обновляет токен приложения """
        self.key = None
        return self.save()

    def generate_key(self):
        """ Генерирует токен приложения """
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
