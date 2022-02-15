from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

from general.models import Requester, RequesterApprovalState


def sendmail(request, requester_id):
    approval_obj = RequesterApprovalState.objects.filter(
        requester_key_id=requester_id,
        request_approved=False,
        state=1
    ).order_by('hirearchy_position')[0]

    subject = 'Requester Form approval'
    active_link = request.build_absolute_uri(
        reverse(
            'requester_update',
            kwargs=dict(
            id=requester_id)
        )
    )
    html_message = render_to_string(
        'requester/email/approval_email.html',
        {
            'first_name': approval_obj.approval_hirearchy.user.first_name,
            'last_name': approval_obj.approval_hirearchy.user.last_name,
            'active_link': active_link
        }
    )
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = [approval_obj.approval_hirearchy.user.email]
    try:
        send_mail(subject,plain_message,from_email,to, html_message=html_message)
    except Exception:
        pass