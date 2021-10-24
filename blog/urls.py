from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
     path('<slug:slug>', views.blog_details, name='blog_details'),
   
]
