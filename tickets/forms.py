from django import forms
from general.constants import PRIORITY_TYPES, URGENCY_TYPES, STATUS_TYPES, SOURCE_TYPES, TICKET_STATE


class TicketForm(forms.Form):
    priority_types = forms.ChoiceField(
        choices=PRIORITY_TYPES,
        label='priority_types',
        required=True
    )
    urgency_types = forms.ChoiceField(
        choices=URGENCY_TYPES,
        label='urgency_types',
        required=True
    )
    ticket_state = forms.ChoiceField(
        choices=TICKET_STATE,
        label='ticket_state',
        required=True
    )
    status_types = forms.ChoiceField(
        choices=STATUS_TYPES,
        label='status_types',
        required=True
    )
    source_types = forms.ChoiceField(
        choices=SOURCE_TYPES,
        label='source_types',
        required=True
    )
    subject = forms.CharField(
        label='Subject',
        max_length=500,
        required=True
    )
    description = forms.CharField(
        label='Description',
        max_length=1000,
        required=True
    )
    expiry_date = forms.DateField(
        label='Ticket Expiry Date',
        required=True
    )
