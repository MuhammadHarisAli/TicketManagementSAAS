from django import forms


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


class RequesterForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=255,
        required=True
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=255,
        required=True
    )
    email = forms.EmailField(
        label='Eemail',
        max_length=255,
        required=True
    )
    job_title = forms.CharField(
        label='Job Title',
        max_length=255,
        required=True
    )
    temporary_user = forms.BooleanField(
        label='Temporary User',
        required=True
    )
    additional_comment = forms.CharField(
        label='Additional Comment',
        max_length=255,
        required=False
    )


class AdminRequesterApprovalHirearchyForm(forms.Form):
    department_hirearchy_position = forms.IntegerField(
        label='Department Hirearchy Position',
        required=True
    )
    department = forms.IntegerField(
        label='Department',
        required=True
    )
    user = forms.IntegerField(
        label='User',
        required=True
    )