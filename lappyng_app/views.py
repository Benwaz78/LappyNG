from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'frontend//index.html')

def about(request):
    return render(request, 'frontend/about.html')

def blog(request):
    return render(request, 'frontend/blog.html')

def blog_details(request):
    return render(request, 'frontend/blog_post.html')


def contact(request):
    return render(request, 'frontend/contact.html')


def product(request):
    return render(request, 'frontend/product.html')


def category_grid(request):
    return render(request, 'frontend/category_grid.html')

def category_list(request):
    return render(request, 'frontend/category_list.html')

def login(request):
    return render(request, 'frontend/login.html')
