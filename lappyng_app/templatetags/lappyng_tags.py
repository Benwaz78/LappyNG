from django import template
from lappyng_app.models import *

register = template.Library()


@register.inclusion_tag('frontend/lappyng_tags/menu-tag.html')
def display_menu():
	categories = Category.objects.all()
	return {'categories_on_menu':categories}


@register.inclusion_tag('frontend/lappyng_tags/brand-sidebar-tag.html')
def list_brand_on_sidebar():
	brands = Brand.objects.all()
	return {'brands':brands}

