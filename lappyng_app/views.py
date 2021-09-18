from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from lappyng_app.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from lappyng_app.forms import *
from django.conf import settings
from django.contrib import messages
from django.db.models import Count, Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    news  = BlogPost.objects.order_by('-created')[:4]
    banner = Banner.objects.order_by('-created')
    new_product = Products.objects.filter(new_product=True)[:4]
    hot_deal = Products.objects.filter(hot_deal=True)[:3]
    new = Products.objects.filter(new=True)[:5]
    products = Products.objects.all()
    context ={
    'news':news, 
    'new_product': new_product,
    'banner':banner,
    'hots': hot_deal,
    'new': new,
    'products':products
    }
    return render(request, 'frontend/index.html', context)

def about(request):
    about_us = About.objects.all()
    return render(request, 'frontend/about.html',  {'abt':about_us})

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


def product(request):
    return render(request, 'frontend/product.html')


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

def category_list(request):
    return render(request, 'frontend/category_list.html')

def login(request):
    return render(request, 'frontend/login.html')
