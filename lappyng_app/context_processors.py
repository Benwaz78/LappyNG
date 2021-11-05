from django.core.paginator import Page
from lappyng_app.models import *
from lappyng_app.forms import *



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