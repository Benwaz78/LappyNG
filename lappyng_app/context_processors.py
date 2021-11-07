from django.core.paginator import Page
from lappyng_app.models import *
from lappyng_app.forms import *
from django.conf import settings
from django.template.loader import render_to_string




def search_form(request):
    return {'form':SearchForm}

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def footer_pages(request):
    list_pages = Pages.objects.order_by('created_at')
    return {'list':list_pages}

def get_uri(request):
    if request.is_secure():
        protocol = 'https://'
    else:
        protocol = 'http://'
    return {'url':'https://lappy.ng'}


def whatsapp_message(request):
    whatsapp = settings.WHATSAPP_NUMBER
    return {'whatsapp':whatsapp}


def contact_info(request):
    contact = ContactInfo.objects.first()
    return {'contact':contact}

def contact_email_template(request):
    contact = ContactInfo.objects.first()
    return render_to_string('frontend/email_templates/email_base.html', {'email_contact':contact}, request=request)