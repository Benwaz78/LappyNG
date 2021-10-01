from django.contrib import admin
from lappyng_app.models import *
from django.utils.html import format_html


admin.site.site_header = 'LappyNG'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def show_cat_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.cat_img.url))

    show_cat_img.short_description = 'Category'

    list_display = [
        'parent',
        'cat_name',
        'slug',
        'show_cat_img',
        'created',

        ]
    prepopulated_fields = {'slug': ('cat_name',)}

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'rating',
        'product',
        'review',
        'created_at',
        'updated',
        ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    def show_brand_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.brand_img.url))

    show_brand_img.short_description = 'Brand'

    list_display = [
        'brand_name',
        'slug',
        'show_brand_img',
        'created',

        ]
    prepopulated_fields = {'slug': ('brand_name',)}



@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    def show_image1(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.image1.url))

    show_image1.short_description = 'Products'

    list_display = [

        'title',
        'slug',
        'show_image1',
        'price',
        'in_stock',
        'is_active',
        'best_seller',
        'created',
        ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def abt_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.image.url))

    abt_img.short_description = 'About'

    list_display = [

        'title',
        'created',
        'modified',

        ]


@admin.register(Banner) 
class Banner(admin.ModelAdmin):

    def post_img(self, obj):
        return format_html('<img src="{}" width="150" />'.format(obj.slide_img.url))

    post_img.short_description = 'Banner'

    list_display = [
        'post_img',
        'slide_content1', 
        'created',
        
        ]