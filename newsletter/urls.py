from django.urls import path
from newsletter import views

app_name = 'newsletter'

urlpatterns = [
    path('', views.newsletters_email, name='newsletters_email'),
    path('letter', views.letter, name='letter'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),
]