from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from general.constants import USER_TYPES


class Profile(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.SmallIntegerField(
            verbose_name=_('User type'),
            choices=USER_TYPES,
            default=1,
        )
    mobile_number = models.CharField(
        verbose_name=_('Mobile number'),
        max_length=255,
        null=True,
        blank=True
    )
    img = models.ImageField(
        upload_to="images/",
        null=True,
        blank=True
    )
    address = models.CharField(
        verbose_name=_('Address'),
        max_length=255,
        null=True,
        blank=True
    )