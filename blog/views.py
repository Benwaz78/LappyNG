from multiprocessing import get_context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from blog.models import *
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

from django.views.generic import(
    ListView, DetailView,
    CreateView, FormView,
    TemplateView, View
)




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

def blog_details(request, slug):
    about_us = About.objects.all()
    most_recent = BlogPost.objects.order_by('created')[:6]
    # most_recent_comment = Comment.objects.filter(post=pk).order_by('-created_on')[:4]
    single_post = get_object_or_404(BlogPost,  slug=slug)
    # comments = Comment.objects.filter(post=pk).order_by('-created_on')
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
        # 'comm':comments, 
        'form':form,
        'single':single_post, 
        # 'abt':about_us, 
        'sipst':single_post,
        # 'most_recent_comment':most_recent_comment,
        # 'pop':popular

        
        })
