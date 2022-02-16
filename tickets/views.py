import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from accounts.models import Profile
from tickets.forms import TicketForm
from tickets.models import Tickets

SOURCE_TYPES = [
    {'id': 1, 'name': 'Phone'},
    {'id': 2, 'name': 'Whatsapp'},
    {'id': 3, 'name': 'FB'},
    {'id': 4, 'name': 'Other'}
]

STATUS_TYPES = [
    {'id': 1, 'name': 'Open'},
    {'id': 2, 'name': 'Pending'},
    {'id': 3, 'name': 'Resolved'},
    {'id': 4, 'name': 'Closed'}
]

URGENCY_TYPES = [
    {'id': 1, 'name': 'Low'},
    {'id': 2, 'name': 'Medium'},
    {'id': 3, 'name': 'High'}
]

PRIORITY_TYPES = [
    {'id': 1, 'name': 'Low'},
    {'id': 2, 'name': 'Medium'},
    {'id': 3, 'name': 'High'},
    {'id': 4, 'name': 'Urgent'}
]

TICKET_STATE = [
    {'id': 1, 'name': 'Tickets on Hold'},
    {'id': 2, 'name': 'Unassigned Tickets'},
    {'id': 3, 'name': 'Ticket IM Wathing'},
    {'id': 4, 'name': 'Overdue Tickets'},
    {'id': 5, 'name': 'Open Tickets'},
    {'id': 6, 'name': 'Ticket Due Today'},
    {'id': 7, 'name': 'In Progress Tickets'},
    {'id': 8, 'name': 'Accelated Tickets'},
    {'id': 9, 'name': 'Closed Tickets'},
    {'id': 10, 'name': 'Cancelled Tickets'},
]

@login_required(login_url='login')
def index(request, *args, **kwargs):
    template = loader.get_template('tickets/index.html')
    context = {
        'tickets_on_hold': Tickets.objects.filter(state=1, created_by_id=request.user.id, ticket_state=1).count(),
        'unassigned_tickets': Tickets.objects.filter(state=1, created_by_id=request.user.id, ticket_state=2).count(),
        'tickets_im_watching': Tickets.objects.filter(state=1, created_by_id=request.user.id, ticket_state=3).count(),
        'overdue_tickets': Tickets.objects.filter(state=1, created_by_id=request.user.id, ticket_state=4).count(),
        'open_tickets': Tickets.objects.filter(state=1, created_by_id=request.user.id, ticket_state=5).count(),
        'tickets_due_today': Tickets.objects.filter(state=1, created_by_id=request.user.id, ticket_state=6).count(),
        'in_progress_tickets': Tickets.objects.filter(state=1, created_by_id=request.user.id, ticket_state=7).count(),
        'accelated_tickets': Tickets.objects.filter(state=1, created_by_id=request.user.id, ticket_state=8).count(),
        'cloased_tickets': Tickets.objects.filter(state=1, created_by_id=request.user.id, ticket_state=9).count(),
        'cancelled_tickets': Tickets.objects.filter(state=1, created_by_id=request.user.id, ticket_state=10).count(),
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def tickets(request, *args, **kwargs):
    template = loader.get_template('tickets/ticketlist.html')
    sidebar_filter_by = request.GET.get('sidebar_filter_by')

    ticket_state = request.GET.get('ticket_state')
    source_type = request.GET.get('source')
    status_type = request.GET.get('status')
    urgency_type = request.GET.get('urgency')
    priority_type = request.GET.get('priority')
    if ticket_state or source_type or status_type or urgency_type or priority_type:
        ticket_list = Tickets.objects.filter(
            state=1,
            created_by_id=request.user.id,
            ticket_state=request.GET.get('ticket_state'),
            source_type=request.GET.get('source'),
            status_type=request.GET.get('status'),
            urgency_type=request.GET.get('urgency'),
            priority_type=request.GET.get('priority'),
        )
    else:
        ticket_list = Tickets.objects.filter(
            state=1,
            created_by_id=request.user.id,
        )
    if sidebar_filter_by:
        ticket_list = ticket_list.filter(ticket_state=sidebar_filter_by,state=1)
    context = {
        'success': True,
        'ticket_list': ticket_list,
        'source_types': SOURCE_TYPES,
        'status_types': STATUS_TYPES,
        'urgency_types': URGENCY_TYPES,
        'priority_types': PRIORITY_TYPES,
        'ticket_state': TICKET_STATE
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def ticketsCreate(request, *args, **kwargs):
    template = loader.get_template('tickets/ticketcreate.html')
    data = {}
    ticket_form = TicketForm(
        initial={
            'priority_types': '',
            'urgency_types': '',
            'status_types': '',
            'source_types': '',
            'subject': '',
            'description': '',
            'created_by': '',
            'assigned': '',
            'ticket_state': '',
            'expiry_date': ''
        }
    )
    if request.method == 'POST':
        data['agent'] = request.POST.get('agent')
        data['subject'] = request.POST.get('subject')
        data['description'] = request.POST.get('description')
        data['source_types'] = request.POST.get('source_types')
        data['priority_types'] = request.POST.get('priority_types')
        data['urgency_types'] = request.POST.get('urgency_types')
        data['status_types'] = request.POST.get('status_types')
        data['ticket_state'] = request.POST.get('ticket_state')
        data['expiry_date'] = request.POST.get('expiry_date')
        ticket_form = TicketForm(data)
        if ticket_form.is_valid():
            Tickets.objects.create(
                subject=data['subject'],
                agent_id=data['agent'],
                description=data['description'],
                source_type=data['source_types'],
                priority_type=data['priority_types'],
                urgency_type=data['urgency_types'],
                status_type=data['status_types'],
                ticket_state=data['ticket_state'],
                expiry_date=data['expiry_date'],
                created_by_id=request.user.id,
                modified_by_id=request.user.id
            )
            return redirect("tickets")

    context = {
        'success': True,
        'ticket_form': ticket_form,
        'user_list': Profile.objects.filter(is_active=True),
        'source_types': SOURCE_TYPES,
        'status_types': STATUS_TYPES,
        'urgency_types': URGENCY_TYPES,
        'priority_types': PRIORITY_TYPES,
        'ticket_state': TICKET_STATE
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def ticketsUpdate(request, *args, **kwargs):
    template = loader.get_template('tickets/ticketcreate.html')
    update_id = kwargs.get('id')
    obj = Tickets.objects.filter(id=update_id, created_by_id=request.user.id)[0]
    data = {}

    ticket_form = TicketForm(
        initial={
            'priority_types': obj.priority_type,
            'urgency_types': obj.urgency_type,
            'status_types': obj.status_type,
            'source_types': obj.source_type,
            'subject': obj.subject,
            'description': obj.description,
            'created_by': obj.created_by,
            'ticket_state': obj.ticket_state,
            'expiry_date': obj.expiry_date
        }
    )
    if request.method == 'POST':
        data['agent'] = request.POST.get('agent')
        data['subject'] = request.POST.get('subject')
        data['description'] = request.POST.get('description')
        data['source_types'] = request.POST.get('source_types')
        data['priority_types'] = request.POST.get('priority_types')
        data['urgency_types'] = request.POST.get('urgency_types')
        data['status_types'] = request.POST.get('status_types')
        data['ticket_state'] = request.POST.get('ticket_state')
        data['expiry_date'] = request.POST.get('expiry_date')
        ticket_form = TicketForm(data)

        if ticket_form.is_valid():
            obj.subject = data['subject']
            obj.agent_id = data['agent']
            obj.description = data['description']
            obj.source_type = data['source_types']
            obj.priority_type = data['priority_types']
            obj.urgency_type = data['urgency_types']
            obj.status_type = data['status_types']
            obj.ticket_state = data['ticket_state']
            obj.expiry_date = data['expiry_date']
            obj.created_by_id = request.user.id
            obj.modified_by_id = request.user.id
            obj.save()

            return redirect("tickets")

    context = {
        'success': True,
        'ticket_form': ticket_form,
        'agent_assigned': obj.agent.id,
        'user_list': Profile.objects.filter(is_active=True),
        'source_types': SOURCE_TYPES,
        'status_types': STATUS_TYPES,
        'urgency_types': URGENCY_TYPES,
        'priority_types': PRIORITY_TYPES,
        'ticket_state': TICKET_STATE
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def ticketsDelete(request, *args, **kwargs):
    delete_id = kwargs.get('id')
    Tickets.objects.filter(id=delete_id).update(state=-1)
    return redirect("tickets")