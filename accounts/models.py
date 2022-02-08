from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from general.constants import USER_TYPES


class Profile(AbstractUser):
    admin = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    email = models.EmailField(
        _('email address'),
        unique=True
    )
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
    employee_id = models.CharField(
        verbose_name=_('Employee ID'),
        max_length=255,
        null=True,
        blank=True
    )
    job_title = models.CharField(
        verbose_name=_('Job Title'),
        max_length=255,
        null=True,
        blank=True
    )
    department = models.ForeignKey(
        'general.Department',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )
    property = models.ForeignKey(
        'general.Property',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )
