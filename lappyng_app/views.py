from multiprocessing import get_context
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

from django.views.generic import(
    ListView, DetailView,
    CreateView, FormView,
    TemplateView, View
)


class Home(TemplateView):
    template_name = 'frontend/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_prod = []
        prod_dict = Products.objects.values('brand', 'id')
        brands = {product['brand'] for product in prod_dict}
        for brand in brands:
            prod_brand = Products.objects.filter(brand=brand)
            all_prod.append([prod_brand,])
        context['prod_brand'] = all_prod
        context['news'] = BlogPost.objects.order_by('-created')[:4]
        context['banner'] = Banner.objects.order_by('-created')
        context['new_arrival'] = Products.objects.order_by('-created')[:5]
        context['hots'] = Products.objects.filter(hot_deal=True)[:3]
        context['best_seller'] = Products.objects.filter(best_seller=True)[:5]
        context['brand'] = Brand.objects.all()
        context['products'] = Products.objects.all()
        context['abt'] = About.objects.all()
        
       
        return context


def about(request):
    content = About.objects.first()
    about_us = About.objects.all()
    return render(request, 'frontend/about.html',  {'abt':about_us, 'content':content})

def blog(request):
    count_post = BlogPost.objects.filter().count()    
    about_us = About.objects.all()
    most_recent = BlogPost.objects.order_by('created')[:4]
    posts = BlogPost.objects.order_by('-created')
    paginated_filter = Paginator(posts, 6)
    page_number = request.GET.get('page')
    comments = Comment.objects.filter()
    person_page_obj = paginated_filter.get_page(page_number)

    context = {
        'person_page_obj': posts, 
        'most_recent': most_recent,
        'post':posts,
        'abt':about_us,
        'counts': count_post,
        'comm':comments
        
    
    }
    context['person_page_obj'] = person_page_obj  
    person_page_obj = paginated_filter.get_page(page_number)
    
    return render(request, 'frontend/blog.html', context)

def blog_details(request, pk):
    about_us = About.objects.all()
    most_recent = BlogPost.objects.order_by('created')[:6]
    most_recent_comment = Comment.objects.filter(post=pk).order_by('-created_on')[:4]
    single_post = get_object_or_404(BlogPost,  pk=pk)
    comments = Comment.objects.filter(post=pk).order_by('-created_on')
    popular = BlogPost.objects.filter(popular=True)[:4]
    
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = single_post
            comment.save()
            return redirect('lappyng_app:blog_details', pk=single_post.pk)
    else:
        form = CommentForm()     

    return render(request, 'frontend/blog_post.html',{'most_recent':most_recent, 
        'comm':comments, 
        'form':form,
        'single':single_post, 
        'abt':about_us, 
        'sipst':single_post,
        'most_recent_comment':most_recent_comment,
        'pop':popular

        
        })
    

def contact(request):
    return render(request, 'frontend/contact.html')


def product_detail(request, slug):
    product = Products.objects.get(slug=slug)
    category = product.category
    get_product_category = Products.objects.filter(category=category)
    top_sales_sidebar_page1 = Products.objects.filter(best_seller=True)[0:5]
    top_sales_sidebar_page2 = Products.objects.filter(best_seller=True)[5:]
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
            form2.save(commit=False)
            form2.instance.product = product
            form2.save()
            print(form2)
            messages.success(request, 'Request Added')
        form1 = ProductReviewForm(prefix='review')
        
    context = {
                'product_detail':product, 
                'slug':slug, 
                'review':form1, 
                'request_form':form2,
                'review_data':review_data,
                'get_prod_cat':get_product_category,
                'sidebar_page1':top_sales_sidebar_page1,
                'sidebar_page2':top_sales_sidebar_page2,
                'get_sale':get_sale_products
                }
    return render(request, 'frontend/product.html', context)



def category_grid(request,  category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Products.objects.filter(category=category)
    paginated_filter = Paginator(products, 16)
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
    paginated_filter = Paginator(products, 16)
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

def category_list(request):
    return render(request, 'frontend/category_list.html')

def login(request):
    return render(request, 'frontend/login.html')

