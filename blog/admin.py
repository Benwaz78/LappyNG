from django.contrib import admin
from blog.models import *
from django.utils.html import format_html


admin.site.site_header = 'LappyNG'




@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):

    def img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.pst_image.url))
    img.short_description = 'Blog Post'

    list_display = [
        'pst_title',
        'slug',
        'img',
        'user',
        'time',
        'created',
        
        ]

    prepopulated_fields = {'slug': ('pst_title',)}
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
