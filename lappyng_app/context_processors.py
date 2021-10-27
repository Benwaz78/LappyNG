from lappyng_app.models import *
from lappyng_app.forms import *



def search_form(request):
    return {'form':SearchForm}

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def get_uri(request):
    return {'url':'https://lappy.ng/'}