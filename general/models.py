from django.db import models
from django.utils.translation import gettext_lazy as _
from general.constants import STATE_TYPES

class Base(models.Model):
    created_by = models.ForeignKey(
        'accounts.profile',
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_created_by",
    )
    created = models.DateTimeField(
        verbose_name=_('Creation date'),
        auto_now_add=True,
        editable=False,
    )
    modified_by = models.ForeignKey(
        'accounts.profile',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_modified_by",
        null=True,
        blank=True,
    )
    modified = models.DateTimeField(
        verbose_name=_('Update date'),
        auto_now=True,
        editable=False,
    )
    state = models.SmallIntegerField(
        verbose_name=_('Publish state'),
        choices=STATE_TYPES,
        default=1,
    )


class Department(Base):
    name = models.CharField(
        verbose_name=_('Department Name'),
        max_length=255,
    )
    supervisor = models.ForeignKey(
        'accounts.profile',
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_created_by",
    )


class Property(Base):
    location = models.CharField(
        verbose_name=_('Location Name'),
        max_length=255,
    )


class ResourceSubType(Base):
    resource_sub_type_name = models.CharField(
        verbose_name=_('Resource Sub Type Name'),
        max_length=255,
    )


class Resource(Base):
    resource_name = models.CharField(
        verbose_name=_('Resource Name'),
        max_length=255,
    )
    resource_sub_type = models.ManyToManyField(
        'ResourceSubType',
        null=True,
        blank=True,
    )


class Requester(Base):
    user = models.ForeignKey(
        'accounts.profile',
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_created_by",
    )
    temporary_user = models.BooleanField(
        verbose_name=_('Temporary User'),
        default=True
    )
    deactivation_date = models.DateTimeField(
        verbose_name=_('Creation date'),
        editable=True,
        null=True,
        blank=True
    )
    additional_comment = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )
    resource_sub_type = models.ManyToManyField(
        ResourceSubType,
        null=True,
        blank=True,
    )
