from django.shortcuts import render
from newsletter.models import *
import random
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
# Create your views here.



def letter(request):
    return render(request, 'newsletter/newsletter.html')


def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

    
def newsletters_email(request):
    data = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        data['is_taken'] = Subscribers.objects.filter(email__iexact=email, confirmed=False).exists()
        if data['is_taken']:
            data['error_message'] = 'Email already exists but yet to be confirmed.'
        else:
            sub = Subscribers(email=email, conf_num=random_digits())
            sub.save()
            args = {
                'url':request.build_absolute_uri('/newsletter/confirm/'),
                'email':sub.email,
                'conf':sub.conf_num
            }
            html_message = render_to_string('frontend/email_templates/confirm-email-result.html', args)
            plain_message = strip_tags(html_message)
            from_email = settings.FROM_HOST
            subject = 'Email Confirmation'
            mail.send_mail(subject, plain_message, from_email, [sub.email,], html_message=html_message, fail_silently=True)
            data['success'] = 'Thanks, we have sent you a confirmation mail in your inbox, click the link to activate'    
    return JsonResponse(data)

def confirm(request):
    sub = Subscribers.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True

        sub.save()
        return render(request, 'frontend/email_templates/confirm-email.html', {'email': sub.email, 'action': 'added'})
    else:
        return render(request, 'frontend/email_templates/confirm-email.html', {'email': sub.email, 'action': 'denied'})

def delete(request):
    sub = Subscribers.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'website/confirm-email.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'website/confirm-email.html', {'email': sub.email, 'action': 'denied'})



