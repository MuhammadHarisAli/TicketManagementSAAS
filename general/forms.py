from django import forms
from accounts.models import Profile


class PropertyForm(forms.Form):
    location = forms.CharField(
        label='Location Name',
        max_length=255,
        required=True
    )


class DepartmentForm(forms.Form):
    name = forms.CharField(
        label='Department Name',
        max_length=255,
        required=True
    )
    supervisor = forms.CharField(
        label='Supervisor',
        max_length=24,
        required=True
    )

class ResourceForm(forms.Form):
    resource_name = forms.CharField(
        label='Resource Name',
        max_length=255,
        required=True
    )
