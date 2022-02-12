from django.utils.translation import gettext_lazy as _

USER_TYPES = (
    (1, _('Super Admin')),
    (2, _('Admin')),
    (3, _('User')),
    (4, _('Requester')),
)

STATE_TYPES = (
    (-1, _('Deleted')),
    (0, _('Paused')),
    (1, _('Active')),
    (2, _('For Review')),
    (3, _('Expired')),
    (4, _('Cancelled')),
)
