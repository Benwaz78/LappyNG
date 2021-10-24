from django.contrib import admin
from newsletter.models import *

# Register your models here.


def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)


send_newsletter.short_description = "Send selected Newsletters to all subscribers"


@admin.register(NewsLetterCategory)
class NewsLetterAdmin(admin.ModelAdmin):
    actions = [send_newsletter, ]
admin.site.register(NewsLetter)
admin.site.register(Subscribers)


