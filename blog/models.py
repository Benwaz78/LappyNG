from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce import HTMLField
import datetime


class BlogPost(models.Model):
    FEATURE = 'Feature'
    NO_FEATURE = 'No Feature'
    CHOOSE = ''
    APPEAR_HOME_FIELD=[
        (FEATURE, 'Appear on home'),
        (NO_FEATURE, "Don't show on home"),
        (CHOOSE, 'Please Choose')
    ]
    pst_title = models.CharField(max_length=150, verbose_name='Post Title')
    slug = models.SlugField(unique=True)
    pst_image = models.ImageField('Post Image', upload_to='uploads/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Posted By')
    content = HTMLField('Content')
    appear_home = models.CharField(max_length=50, choices=APPEAR_HOME_FIELD, default=CHOOSE)
    created = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    today = datetime.date.today()
    months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']
    current_month = months[today.month]
    popular= models.BooleanField( verbose_name='Popular Post')
    
    
    def __str__(self):
        return self.pst_title

    class Meta():
        verbose_name_plural = '5. Blog Post'

    @property
    def img_url(self):
        if self.pst_image:
            return self.pst_image.url
    
    @property
    def get_comments(self):
        return self.comments.all()

    @property
    def get_comments_count(self):
        return self.comments.count

    def get_post_url(self):
        return reverse('blog:blog_details', kwargs={
            'slug': self.slug,
        })



class Comment(models.Model):
    name = models.CharField(max_length=80,verbose_name= 'Name')
    email = models.EmailField()
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    class Meta():
        verbose_name_plural = '6. Comments'


    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

