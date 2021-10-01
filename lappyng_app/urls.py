from django.urls import path
from lappyng_app import views

app_name = 'lappyng_app'

urlpatterns = [
    path('blog-page/', views.blog, name='blog'),
    path('blog-slug/<int:pk>', views.blog_details, name='blog_details'),
    path('<slug:slug>/', views.product_detail, name='product'),
    path('category_grid-page/<slug:category_slug>/', views.category_grid, name='category_grid'),
    path('brand-list-page/<slug:brand_slug>/', views.brand_list, name='brand_list'),
    path('category_list-page/', views.category_list, name='category_list'),
    path('login-page/', views.login, name='login'),
]
