from django.db import models
from lappyng_app.models import *
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

# Create your models here.

class Subscribers(models.Model):
    email = models.EmailField()
    conf_num = models.CharField(max_length=30)
    confirmed = models.BooleanField(default=False)

    class Meta():
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email + " (" + str(self.confirmed) + ")"


class NewsLetterCategory(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + self.created_at.strftime("%B %d, %Y")

    class Meta():
        verbose_name_plural = 'Newsletter Category'


    def send(self, request):
        subscribers = Subscribers.objects.filter(confirmed=True)
        news_letters_list = []
        news = NewsLetter.objects.filter(news_letter__id=self.id)
        for value in news:
            news_letters_list.append(
                {'title': value.product.title, 
                'content': value.product.contents, 
                'image': value.product.image1,
                'link': request.build_absolute_uri('/products/detail/')+value.product.slug,
                })

        # goes through all post and adds it to the newsletter dictionary

        for sub in subscribers:
            html_message = render_to_string('frontend/email_templates/newsletter.html', 
                {
                'news': news_letters_list, 
                'url':request.build_absolute_uri('/newsletter/delete/'),
                'email':sub.email,
                'conf':sub.conf_num
                })
            plain_message = strip_tags(html_message)
            from_email = settings.FROM_HOST
            mail.send_mail('From Lappyng', plain_message, from_email, [sub.email, ], html_message=html_message)
        return "done"


class NewsLetter(models.Model):
    news_letter = models.ForeignKey(NewsLetterCategory, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

    def __repr__(self):
        return self.product.title

  
