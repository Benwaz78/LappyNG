from multiprocessing import get_context
from django.db import connections
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from lappyng_app.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import sys

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from lappyng_app.forms import *
from django.conf import settings
from django.contrib import messages
from django.db.models import Count, Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from lappyng_app.context_processors import contact_info, get_uri
from django.core.serializers import serialize
# from django.core.serializers.json import LazyE

from django.views.generic import(
    ListView, DetailView,
    CreateView, FormView,
    TemplateView, View
)

from django.utils.html import format_html


class Home(TemplateView):
    template_name = 'frontend/index.html'
    def get_context_data(self, **kwargs):
        brand =  Brand.objects.first()
        brand_id = brand.id
        context = super().get_context_data(**kwargs)
        context['news'] = BlogPost.objects.order_by('-created')[:4]
        context['banner'] = Banner.objects.order_by('-created')
        context['new_arrival'] = Products.objects.order_by('-created')
        context['best_seller'] = Products.objects.filter(best_seller=True)[:5]
        context['new_arrival1'] = Products.objects.order_by('-created')[0:3]
        context['new_arrival2'] = Products.objects.order_by('-created')[3:5]
        context['hots'] = Products.objects.filter(hot_deal=True)[:3]
        context['brand'] = Brand.objects.all()
        context['products'] = Products.objects.all()
        context['abt'] = About.objects.all()
        context['top_banner1'] = HomeTopBanner.objects.first()
        context['top_banner2'] = HomeTopBanner.objects.last()
        context['two_side_banner'] = HomeTwoSideBanner.objects.all()[:2]
        context['sidebar_banner'] = HomeSideBanner.objects.first()
        context['last_brand_id'] = brand_id
        context['last_product'] = Products.objects.filter(brand__id=brand_id)[:5]
        return context
    
    def post(self, request, *args, **kwargs):
        data = {}
        id = request.POST.get('id')
        context = {
                    'query':Products.objects.filter(brand__id=id)[:5],
                }
        data['html'] = render_to_string('frontend/product-brand-partial.html', context)
        return JsonResponse(data, safe=False)



def about(request):
    content = About.objects.first()
    about_us = About.objects.all()
    return render(request, 'frontend/about.html',  {'abt':about_us, 'content':content})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        subject = 'lappy.ng Contact Form'
        context = {
            'name':name,
            'email':email,
            'phone':phone,
            'message': message,
        }
        
        html_message = render_to_string('frontend/email_templates/contact-email-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = settings.FROM_HOST
        send = mail.send_mail(subject, plain_message, from_email, settings.RECIEVER_MAIL, html_message=html_message, fail_silently=False)
        with mail.get_connection(backend=None, fail_silently=False) as connection:
            mail.EmailMessage(
                subject, plain_message, from_email, settings.RECIEVER_MAIL,connection=connection,).send()
        if send:
            messages.success(request, 'Email sent succesfully!')
        else:
            messages.error(request, 'Mail not sent!')
    return render(request, 'frontend/contact.html')








def product_detail(request, slug):
    product = Products.objects.get(slug=slug)
    category = product.category
    get_product_category = Products.objects.filter(category=category)
    top_sales_sidebar_page1 = Products.objects.filter(best_seller=True)[0:3]
    top_sales_sidebar_page2 = Products.objects.filter(best_seller=True)[3:6]
    get_sale_products = Products.objects.filter(is_active=True)
    form1 = ProductReviewForm(prefix='review')
    form2 = ProductRequestForm(prefix='request')
    review_data = ProductReview.objects.filter(product__slug=slug).order_by('-created_at')
    slug = product.slug
    data = {}
    if request.method and request.POST.get('hidden_form') == 'review_hidden':
        form1 = ProductReviewForm(request.POST, prefix='review')
        if form1.is_valid():
            form1.save(commit=False)
            form1.instance.product = product
            form1.save()
            data['success'] = 'Review Created'
            data['html_data'] = render_to_string('frontend/review-partial.html', {'review_data':review_data, 'slug':slug})
            return JsonResponse(data)
        form2 = ProductRequestForm(prefix='review')
    elif request.method and request.POST.get('hidden_form') == 'request_hidden':
        form2 = ProductRequestForm(request.POST, prefix='request')
        if form2.is_valid():
            name = form2.cleaned_data.get('name')
            email = form2.cleaned_data.get('email')
            phone = form2.cleaned_data.get('phone')
            description = form2.cleaned_data.get('description')
            product_image = product.image1
            form2.save(commit=False)
            form2.instance.product = product
            form2.save()
            reciever_subject = 'Order Form'
            reciever_context = {
                'name':name,
                'email':email,
                'phone':phone,
                'email':email,
                'description': description,
                'image':product_image,
                'product_name':product.title,
                'product_price':product.price,
                'discount_price':product.discount_prize(),
                'brand':product.brand,
                'category':product.category,
            
            }
            reciever_html_message = render_to_string('frontend/email_templates/reciever-template.html', reciever_context)
            reciever_plain_message = strip_tags(reciever_html_message)
            reciever_from_email = settings.FROM_HOST
            

            sender_context = {
                'name':name,
                'image':product_image,
                'product_name':product.title,
                'product_price':product.price,
                'discount_price':product.discount_prize(),
                'brand':product.brand,
                'category':product.category,
            }
            sender_html_message = render_to_string('frontend/email_templates/sender-template.html', sender_context)
            sender_plain_message = strip_tags(sender_html_message)
            sender_from_email = settings.FROM_HOST
    
            with mail.get_connection() as connection:
                sender_send = mail.EmailMultiAlternatives(reciever_subject, sender_plain_message, sender_from_email, 
                        [email,], connection=connection)
                sender_send.attach_alternative(sender_html_message, "text/html")
                sender_send.send()
                reciever_send = mail.EmailMultiAlternatives(reciever_subject, reciever_plain_message, reciever_from_email, 
                        settings.RECIEVER_MAIL, connection=connection)
                reciever_send.attach_alternative(reciever_html_message, "text/html")
                reciever_send.send()
                message = format_html('<strong>Thanks!</strong> Please check your mail to see your order details')
                messages.success(request, message)



        form1 = ProductReviewForm(prefix='review')
        
    context = {
                'product_detail':product, 
                'slug':slug, 
                'review':form1, 
                'request_form':form2,
                'get_category':category,
                'review_data':review_data,
                'get_prod_cat':get_product_category,
                'sidebar_page1':top_sales_sidebar_page1,
                'sidebar_page2':top_sales_sidebar_page2,
                'get_sale':get_sale_products
                }
    return render(request, 'frontend/product.html', context)




def search_result(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            category = form.cleaned_data.get('category')
            query_filter = Products.objects.filter(Q(title__contains=title) | Q(category=category))
            return render(request, 'frontend/search-result.html', {'query':query_filter})
    return render(request, 'frontend/search-result.html')


def detail_page(request, slug):
    page = Pages.objects.get(slug=slug)
    return render(request, 'frontend/page.html', {'single_page':page})


def category_grid(request,  category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Products.objects.filter(category=category)
    paginated_filter = Paginator(products, 4)
    page_number = request.GET.get('page')
    about_us = About.objects.all()
    person_page_obj = paginated_filter.get_page(page_number)

    context = {
        'category' : category, 
        'products' : products, 
        'person_page_obj': products,
        'about_us':about_us
    }

    context['person_page_obj'] = person_page_obj  
    person_page_obj = paginated_filter.get_page(page_number)
    return render(request, 'frontend/category_grid.html' , context)

def brand_list(request,  brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    products = Products.objects.filter(brand=brand)
    paginated_filter = Paginator(products, 4)
    page_number = request.GET.get('page')
    about_us = About.objects.all()
    person_page_obj = paginated_filter.get_page(page_number)

    context = {
        'brand' : brand, 
        'products' : products, 
        'person_page_obj': products,
        'about_us':about_us
    }

    context['person_page_obj'] = person_page_obj  
    person_page_obj = paginated_filter.get_page(page_number)
    return render(request, 'frontend/brand-list.html' , context)


def order_template(request):
    return render(request, 'frontend/email_templates/order-email-template.html')


def contact_template(request):
    return render(request, 'frontend/email_templates/contact-email-template.html')

def newsletter_template(request):
    return render(request, 'frontend/email_templates/newsletter.html')


def category_list(request):
    return render(request, 'frontend/category_list.html')

def login(request):
    return render(request, 'frontend/login.html')








