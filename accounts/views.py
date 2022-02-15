from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from django.http import Http404, HttpResponse, JsonResponse
from django.template import loader

from accounts.models import Profile
from .forms import LoginForm, ProfileForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


@login_required(login_url='login')
def createuser(request):
    template = loader.get_template('accounts/create-user.html')
    data = {}
    profile_form = ProfileForm(
        initial={
            'name': '',
            'telephone_number': '',
            'email': '',
            'address': '',
            'image': '',
            'password': '',
        }
    )

    if request.method == 'POST':
        data['name'] = request.POST.get('name')
        data['telephone_number'] = request.POST.get('phone-number')
        data['email'] = request.POST.get('email')
        data['address'] = request.POST.get('address')
        data['password'] = make_password(request.POST.get('password'))
        data['image'] = request.POST.get('customFile')
        profile_form = ProfileForm(data)
        if profile_form.is_valid():
            Profile.objects.create(
                email=data['email'],
                username=data['name'],
                mobile_number=data['telephone_number'],
                password=data['password'],
                img=data['image'],
                address=data['address'],
                user_type=2
            )
    context = {
        'success': True,
        'profile_form': profile_form,
        'admin_list': Profile.objects.filter(user_type=2, is_active=True)
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def adminlist(request):
    template = loader.get_template('accounts/admin_list.html')
    context = {
        'success': True,
        'admin_list': Profile.objects.filter(user_type=2, is_active=True)
    }
    return HttpResponse(template.render(context, request))