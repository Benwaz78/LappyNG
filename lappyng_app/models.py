from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce import HTMLField
import datetime
from decimal import Decimal as D

class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    cat_name = models.CharField(max_length=100, unique=True, verbose_name='Category')
    slug = models.SlugField(unique=True)
    cat_img = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='Category Image', help_text='Use this Image dimension 170px X 100px')
    cat_img_banner = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='Category Banner Image', help_text='Use this Image dimension 848px X 132px')
    cat_img_banner2 = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='Category Banner Image', help_text='Use this Image dimension 848px X 132px')
    created = models.DateTimeField(auto_now_add=True)
    
    def show_cat_img(self):
        if self.cat_img:
            return self.cat_img.url
        else:
            return 'frontend/images/media/index1/img-category2.jpg'

    def show_cat_img_banner(self):
        if self.cat_img_banner:
            return self.cat_img_banner.url
    
    def show_cat_img_banner2(self):
        if self.cat_img_banner2:
            return self.cat_img_banner2.url

    def get_absolute_url(self):
        return reverse('lappyng_app:category_grid', args=[self.slug])

    def __str__(self):
        return self.cat_name

    

    class Meta():
        verbose_name_plural = '1. Category'
        ordering = ['-created',]

    def save(self, *args, **kwargs):
        self.cat_name = self.cat_name.capitalize()
        return super().save(*args, **kwargs)

class Brand(models.Model):
    brand_name = models.CharField(max_length=30, unique=True, verbose_name='Brand')
    slug = models.SlugField(unique=True)
    brand_img = models.ImageField(blank=True, null=True, verbose_name='Brand Image', help_text='Use this Image dimension 157px X 88px')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand_name

    class Meta():
        verbose_name_plural = '2. Brand'
        ordering = ['-created',]
    
    def show_brand_img(self):
        if self.brand_img:
            return self.brand_img.url
        else:
            return 'prairiemartapp/images/media/index1/top-brand2.png'

    def get_absolute_url(self):
        return reverse('lappyng_app:brand_list', args=[self.slug])

    def save(self, *args, **kwargs):
        self.cat_name = self.brand_name.capitalize()
        return super().save(*args, **kwargs)


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(Q(is_active=True) | Q(percent=True))

class Products(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='product_brand', null=True, blank=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    price = models.FloatField(verbose_name='Price')
    percent = models.PositiveIntegerField(blank=True, null=True, verbose_name='Percentage Discount', help_text='Example 30%')
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    new_product = models.BooleanField()
    hot_deal = models.BooleanField( verbose_name='Hot Deals of this Week', blank=True, null=True)
    best_seller = models.BooleanField(blank=True, null=True, default=False)
    image1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    contents = HTMLField('Content')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = models.Manager()
    
    

    class Meta:
        verbose_name_plural='3. Products'
        ordering = ('-created',)
    

    def discount_prize(self):
        if self.percent is not None:
            dis = self.price - self.price * self.percent/100
            return dis

    def show_image1(self):
        if self.image1:
            return self.image1.url
        else:
            return 'prairiemartapp/images/media/index1/top-brand2.png'

    def show_image2(self):
        if self.image2:
            return self.image2.url
        else:
            return 'prairiemartapp/images/media/index1/top-brand2.png'

    def show_image3(self):
        if self.image3:
            return self.image3.url
        else:
            return 'prairiemartapp/images/media/index1/top-brand2.png'
    
    def get_absolute_url(self):
        return reverse('lappyng_app:product', args=[self.slug])

    def __str__(self):
        return self.title

class ProductRequest(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Product Request'
        ordering = ('-created',)

class ProductReview(models.Model):

    ONE = '10'
    TWO = '20'
    THREE = '30'
    FOUR = '40'
    FIVE = '50'
    SIX = '60'
    SEVEN = '70'
    EIGHT = '80'
    NINE = '90'
    TEN = '100'
    CHOOSE = ''
    RATING_LIST = [
        (ONE, 1),
        (TWO, 2),
        (THREE, 3),
        (FOUR, 4),
        (FIVE, 5),
        (SIX, 6),
        (SEVEN, 7),
        (EIGHT, 8),
        (NINE, 9),
        (TEN, 10),
        (CHOOSE, 'Choose Rating'),
    ]
    full_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    rating = models.CharField(max_length=10, choices=RATING_LIST, default=CHOOSE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def get_ratings(self):
        if self.rating == '10':
            return '10'
        elif self.rating == '20':
            return '20'
        elif self.rating == '30':
            return '30'
        elif self.rating == '40':
            return '40'
        elif self.rating == '50':
            return '50'
        elif self.rating == '60':
            return '60'
        elif self.rating == '70':
            return '70'
        elif self.rating == '80':
            return '80'
        elif self.rating == '90':
            return '90'
        elif self.rating == '100':
            return '100'
    
    def __str__(self):
        return self.full_name

class About(models.Model):
    title = models.CharField(max_length=50)
    abt_content = HTMLField('Content')
    image = models.FileField(null=True, blank=True, upload_to='uploads/')
    image1 = models.FileField( blank=True, upload_to='uploads/')
    image2 = models.FileField( blank=True, upload_to='uploads/')
    image3 = models.FileField( blank=True, upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural='4. About'

    def abt_img(self):
        if self.image:
            return self.image.url

    def abt_img1(self):
        if self.image1:
            return self.image1.url

    def abt_img2(self):
        if self.image2:
            return self.image2.url

    def abt_img3(self):
        if self.image3:
            return self.image3.url



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
        return reverse('lappyng_app:blog_details', kwargs={
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



class Banner(models.Model):
    slide_img = models.FileField(null=True, verbose_name='Slide Image', blank=True, upload_to='uploads/')
    slide_content1 = models.TextField(blank=True, null=True)
    slide_content2 = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.slide_content1[:5]
    
    def post_img(self):
        if self.slide_img:
          return self.slide_img.url

    class Meta():
        verbose_name_plural = 'Banner'


