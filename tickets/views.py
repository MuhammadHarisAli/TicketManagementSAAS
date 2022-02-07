from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse
from django.template import loader


@login_required(login_url='login')
def index(request, *args, **kwargs):
    template = loader.get_template('tickets/index.html')
    context = {}
    return HttpResponse(template.render(context, request))