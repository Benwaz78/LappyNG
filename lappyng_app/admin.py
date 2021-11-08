from django.contrib import admin
from lappyng_app.models import *
from django.utils.html import format_html


admin.site.site_header = 'LappyNG'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'cat_name',
        'slug',
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

@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'product',
        'created',
        'modified',
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

@admin.register(HomeTopBanner)
class HomeTopBannerAdmin(admin.ModelAdmin):
    def get_banner(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.banner.url))

    get_banner.short_description = 'Banner'

    

    list_display = [
        'get_banner',
        'link',
        ]

@admin.register(HomeTwoSideBanner)
class HomeTwoSideBannerAdmin(admin.ModelAdmin):
    def get_banner(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.banner.url))

    get_banner.short_description = 'Banner'

    list_display = [
        'get_banner',
        'link',
        ]

@admin.register(HomeSideBanner)
class HomeSideBannerAdmin(admin.ModelAdmin):
    def get_banner(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.banner.url))

    get_banner.short_description = 'Banner'

    list_display = [
        'get_banner',
        'link',
        ]



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
        'brand',
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


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = [
        'page_title',
        'created_at',
        'updated_at',
        ]
    prepopulated_fields = {'slug': ('page_title',)}


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = [
        'facebook',
        'twitter',
        'phone1',
        'email1',
        'address',
        ]

