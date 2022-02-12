import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.http import Http404, HttpResponse
from django.template import loader

from accounts.models import Profile
from general.forms import PropertyForm, DepartmentForm, ResourceForm, RequesterForm
from general.models import Property, Department, Resource, ResourceSubType, Requester


class PropertyView(TemplateView):
    model = Property

    def get_queryset(self,request):
        queryset = Property.objects.filter(created_by_id=request.user.id, state=1)
        return queryset

    def get(self, request, *args, **kwargs):
        template = loader.get_template('general/propertylist.html')
        context = {
            'success': True,
            'property_list': self.get_queryset(request)
        }
        return HttpResponse(template.render(context, request))



@login_required(login_url='login')
def propertyCreate(request, *args, **kwargs):
    template = loader.get_template('general/propertycreate.html')
    data = {}
    property_form = PropertyForm(
        initial={
            'location': '',
        }
    )
    if request.method == 'POST':
        data['location'] = request.POST.get('location')
        property_form = PropertyForm(data)
        if property_form.is_valid():
            Property.objects.create(
                location=data['location'],
                created_by_id=request.user.id,
                modified_by_id=request.user.id
            )
            return redirect("property")
    context = {
        'success': True,
        'property_form': property_form
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def propertyupdate(request, *args, **kwargs):
    template = loader.get_template('general/propertycreate.html')
    update_id = kwargs.get('id')

    property = Property.objects.filter(id=update_id,created_by_id=request.user.id)[0]
    data = {}
    property_form = PropertyForm(
        initial={
            'location': property.location,
        }
    )
    if request.method == 'POST':
        data['location'] = request.POST.get('location')
        property_form = PropertyForm(data)
        if property_form.is_valid():
            property.location=data['location']
            property.save()
            return redirect("property")
    context = {
        'success': True,
        'property_form': property_form
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def propertyDelete(request, *args, **kwargs):
    delete_id = kwargs.get('id')
    Property.objects.filter(id=delete_id,created_by_id=request.user.id).update(state=-1)
    return redirect("property")



@login_required(login_url='login')
def department(request, *args, **kwargs):
    template = loader.get_template('general/department.html')
    context = {
        'success': True,
        'department_list': Department.objects.filter(state=1),
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def departmentCreate(request, *args, **kwargs):
    template = loader.get_template('general/department_create.html')
    data = {}
    department_form = DepartmentForm(
        initial={
            'name': '',
            'supervisor': ''
        }
    )

    if request.method == 'POST':
        data['name'] = request.POST.get('department')
        data['supervisor'] = request.POST.get('supervisor')
        department_form = DepartmentForm(data)
        if department_form.is_valid():
            Department.objects.create(
                name=data['name'],
                supervisor_id = data['supervisor'],
                created_by_id=request.user.id,
                modified_by_id=request.user.id
            )
            return redirect("department")
    context = {
        'success': True,
        'property_form': department_form,
        'supervisor_list': Profile.objects.filter(is_active=True)
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def departmentupdate(request, *args, **kwargs):
    template = loader.get_template('general/department_create.html')
    update_id = kwargs.get('id')
    department = Department.objects.filter(id=update_id, created_by_id=request.user.id)[0]
    data = {}
    department_form = DepartmentForm(
        initial={
            'name': department.name,
            'supervisor': department.supervisor.id
        }
    )

    if request.method == 'POST':
        data['name'] = request.POST.get('department')
        data['supervisor'] = request.POST.get('supervisor')
        department_form = DepartmentForm(data)
        if department_form.is_valid():
            department.name = data['name']
            department.supervisor_id = data['supervisor']
            department.save()
            return redirect("department")
    context = {
        'success': True,
        'department_form': department_form,
        'supervisor_list': Profile.objects.filter(is_active=True)
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def departmentDelete(request, *args, **kwargs):
    delete_id = kwargs.get('id')
    Department.objects.filter(id=delete_id,created_by_id=request.user.id).update(state=-1)
    return redirect("department")



@login_required(login_url='login')
def resource(request, *args, **kwargs):
    template = loader.get_template('general/resource.html')
    context = {
        'success': True,
        'resource_list': Resource.objects.filter(state=1),
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def resourceCreate(request, *args, **kwargs):
    template = loader.get_template('general/resource_create.html')
    data = {}
    resource_form = ResourceForm(
        initial={
            'resource_name': '',
        }
    )
    if request.method == 'POST':
        data['resource_name'] = request.POST.get('resource_name')
        resource_form = ResourceForm(data)
        if resource_form.is_valid():
            resource = Resource.objects.create(
                resource_name=data['resource_name'],
                created_by_id=request.user.id,
                modified_by_id=request.user.id
            )
            if request.POST.getlist('new_sub_resource_name'):
                for new_sub_resource in request.POST.getlist('new_sub_resource_name'):
                    resource_sub_type = ResourceSubType.objects.create(
                        resource_sub_type_name=new_sub_resource,
                        created_by_id=request.user.id,
                        modified_by_id=request.user.id
                    )
                    resource.resource_sub_type.add(resource_sub_type.id)
            return redirect("resource")
    context = {
        'success': True,
        'resource_form': resource_form,
        'sub_resource': []
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def resourceupdate(request, *args, **kwargs):
    template = loader.get_template('general/resource_create.html')
    update_id = kwargs.get('id')
    resource = Resource.objects.filter(id=update_id, created_by_id=request.user.id)[0]
    data = {}
    resource_form = ResourceForm(
        initial={
            'resource_name': resource.resource_name,
            'id': resource.id,
        }
    )

    if request.method == 'POST':
        data['resource_name'] = request.POST.get('resource_name')
        resource_form = ResourceForm(data)
        if resource_form.is_valid():
            resource.resource_name = data['resource_name']
            resource.save()
            if request.POST.getlist('new_sub_resource_name'):
                for new_sub_resource in request.POST.getlist('new_sub_resource_name'):
                    resource_sub_type = ResourceSubType.objects.create(
                        resource_sub_type_name=new_sub_resource,
                        created_by_id=request.user.id,
                        modified_by_id=request.user.id
                    )
                    resource.resource_sub_type.add(resource_sub_type.id)
            return redirect("resource")
    context = {
        'success': True,
        'resource_form': resource_form,
        'sub_resource': resource.resource_sub_type.filter(state=1, created_by_id=request.user.id)
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def resourceDelete(request, *args, **kwargs):
    delete_id = kwargs.get('id')
    Resource.objects.filter(id=delete_id,created_by_id=request.user.id).update(state=-1)
    return redirect("resource")


@login_required(login_url='login')
def subresourceDelete(request, *args, **kwargs):
    sub_resource_id = kwargs.get('sub_resource_id')
    sub_resource_obj = ResourceSubType.objects.filter(id=sub_resource_id,created_by_id=request.user.id)[0]
    sub_resource_obj.state = -1
    sub_resource_obj.save()
    return redirect(reverse('resource_update',
                        kwargs=dict(
                            id=sub_resource_obj.resource_set.all()[0].id)
                        )
                    )

@login_required(login_url='login')
def requester(request, *args, **kwargs):
    template = loader.get_template('requester/requesterlist.html')
    context = {
        'success': True,
        'requester_list': Requester.objects.filter(state=1, created_by_id=request.user.id),
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def requesterCreate(request, *args, **kwargs):
    template = loader.get_template('requester/requester_create.html')
    data = {}
    requester_form = RequesterForm(
        initial={
            'first_name': '',
            'last_name': '',
            'email': '',
            'job_title': '',
            'temporary_user': False,
            'additional_comment':''
        }
    )
    if request.method == 'POST':
        data['first_name'] = request.POST.get('first_name')
        data['last_name'] = request.POST.get('last_name')
        data['email'] = request.POST.get('email')
        data['job_title'] = request.POST.get('job_title')
        data['temporary_user'] = request.POST.get('temporary_user')
        data['additional_comment'] = request.POST.get('additional_comment')
        requester_form = RequesterForm(data)

        if requester_form.is_valid():

            request_user = Profile.objects.create(
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['first_name'] + str(datetime.datetime.now()),
                department_id=request.POST.get('department'),
                job_title=data['job_title'],
                user_type=4
            )
            for requester_property_id in request.POST.getlist('property'):
                request_user.property.add(requester_property_id)

            requester_obj = Requester.objects.create(
                temporary_user= True if data['temporary_user'] == '0' else False,
                additional_comment=data['additional_comment'],
                created_by_id=request.user.id,
                modified_by_id=request.user.id,
                user_id=request_user.id,
            )
            if requester_obj.temporary_user:
                requester_obj.deactivation_date = request.POST.get('expiry_date')
                requester_obj.save()
            for requester_sub_resource_id in request.POST.getlist('resource'):
                requester_obj.resource_sub_type.add(requester_sub_resource_id)

            return redirect("requester")

    context = {
        'success': True,
        'property_form': requester_form,
        'deepartment_list': Department.objects.filter(state=1, created_by_id=request.user.id),
        'resource_list': Resource.objects.filter(state=1, created_by_id=request.user.id),
        'property_list': Property.objects.filter(state=1, created_by_id=request.user.id)
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def requesterupdate(request, *args, **kwargs):
    template = loader.get_template('requester/requester_create.html')
    update_id = kwargs.get('id')
    requester_obj = Requester.objects.filter(id=update_id)[0]
    data = {}

    if request.method == 'POST':
        data['first_name'] = request.POST.get('first_name')
        data['last_name'] = request.POST.get('last_name')
        data['email'] = request.POST.get('email')
        data['job_title'] = request.POST.get('job_title')
        data['temporary_user'] = request.POST.get('temporary_user')
        data['additional_comment'] = request.POST.get('additional_comment')
        requester_form = RequesterForm(data)

        if requester_form.is_valid():

            requester_obj.user.email=data['email']
            requester_obj.user.first_name=data['first_name']
            requester_obj.user.last_name=data['last_name']
            requester_obj.user.username=data['first_name'] + str(datetime.datetime.now())
            requester_obj.user.department_id=request.POST.get('department')
            requester_obj.user.job_title=data['job_title']

            requester_obj.user.property.clear()
            for requester_property_id in request.POST.getlist('property'):
                requester_obj.user.property.add(requester_property_id)
            requester_obj.user.save()

            requester_obj.temporary_user= True if data['temporary_user'] == '0' else False
            requester_obj.additional_comment=data['additional_comment']
            requester_obj.modified_by_id=request.user.id

            if requester_obj.temporary_user:
                requester_obj.deactivation_date = request.POST.get('expiry_date')
            else:
                requester_obj.deactivation_date = None

            requester_obj.save()
            requester_obj.resource_sub_type.clear()
            for requester_sub_resource_id in request.POST.getlist('resource'):
                requester_obj.resource_sub_type.add(requester_sub_resource_id)
    requester_form = RequesterForm(
        initial={
            'temporary_user': 'true' if requester_obj.temporary_user else 'false',
            'additional_comment': requester_obj.additional_comment,
            'first_name': requester_obj.user.first_name,
            'last_name': requester_obj.user.last_name,
            'selected_department': requester_obj.user.department_id,
            'job_title': requester_obj.user.job_title,
            'email': requester_obj.user.email,
        }
    )
    context = {
        'success': True,
        'requester_form': requester_form,
        'deactivation_date': requester_obj.deactivation_date,
        'deepartment_list': Department.objects.filter(state=1, created_by_id=request.user.id),
        'resource_list': Resource.objects.filter(state=1, created_by_id=request.user.id),
        'property_list': Property.objects.filter(state=1, created_by_id=request.user.id),
        'selected_resource_sub_type': list(requester_obj.resource_sub_type.all().values_list('id', flat=True)),
        'selected_property': list(requester_obj.user.property.all().values_list('id', flat=True))
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def requesterDelete(request, *args, **kwargs):
    delete_id = kwargs.get('id')
    Requester.objects.filter(id=delete_id).update(state=-1)
    return redirect("requester")