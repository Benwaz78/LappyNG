from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag('frontend/blog_tags/sidebar-tag.html')
def recent_post():
	posts = BlogPost.objects.order_by('-created')
	return {'pop':posts}