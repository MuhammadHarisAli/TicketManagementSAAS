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

SOURCE_TYPES = (
    (1, _('Phone')),
    (2, _('Whatsapp')),
    (3, _('FB')),
    (4, _('Other'))
)

STATUS_TYPES = (
    (1, _('Open')),
    (2, _('Pending')),
    (3, _('Resolved')),
    (4, _('Closed'))
)

URGENCY_TYPES = (
    (1, _('Low')),
    (2, _('Medium')),
    (3, _('High'))
)

PRIORITY_TYPES = (
    (1, _('Low')),
    (2, _('Medium')),
    (3, _('High')),
    (3, _('Urgent'))
)