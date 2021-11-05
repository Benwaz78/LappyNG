from django.urls import path
from lappyng_app import views

app_name = 'lappyng_app'

urlpatterns = [
    path('category/<slug:category_slug>/', views.category_grid, name='category_grid'),
    path('brand/<slug:brand_slug>/', views.brand_list, name='brand_list'),
    path('detail/<slug:slug>/', views.product_detail, name='product'),
    path('category_list-page/', views.category_list, name='category_list'),
    path('search-result/', views.search_result, name='search_result'),
    path('login-page/', views.login, name='login'),
    path('order-template/', views.order_template, name='order_template'),
    path('contact-template/', views.contact_template, name='contact_template'),
    path('newsletter-template/', views.newsletter_template, name='newsletter_template'),
]
