from django.db import models
from django.utils.translation import gettext_lazy as _

from general.models import Base
from general.constants import SOURCE_TYPES, STATUS_TYPES, URGENCY_TYPES, PRIORITY_TYPES, TICKET_STATE
# Create your models here.


class Tickets(Base):
    subject = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )
    source_type = models.SmallIntegerField(
        verbose_name=_('User type'),
        choices=SOURCE_TYPES,
        default=1,
    )
    status_type = models.SmallIntegerField(
        verbose_name=_('User type'),
        choices=STATUS_TYPES,
        default=1,
    )
    urgency_type = models.SmallIntegerField(
        verbose_name=_('User type'),
        choices=URGENCY_TYPES,
        default=1,
    )
    priority_type = models.SmallIntegerField(
        verbose_name=_('User type'),
        choices=PRIORITY_TYPES,
        default=1,
    )
    agent = models.ForeignKey(
        'accounts.profile',
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_created_by",
    )
    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )
    ticket_state = models.SmallIntegerField(
        verbose_name=_('Publish state'),
        choices=TICKET_STATE,
        default=1,
    )
    expiry_date = models.DateTimeField(
        verbose_name=_('Creation date'),
        editable=True,
        null=True,
        blank=True
    )