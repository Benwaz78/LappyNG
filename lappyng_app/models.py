from tabnanny import verbose
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime
from decimal import Decimal as D
from django.utils.html import format_html
from cloudinary.models import CloudinaryField

class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True, verbose_name='Category')
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
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
    brand_img = CloudinaryField('Brand Image', blank=True, null=True, help_text='Use this Image dimension 157px X 88px')
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
    image1 = CloudinaryField()
    image2 = CloudinaryField(blank=True, null=True)
    image3 = CloudinaryField(blank=True, null=True)
    contents = HTMLField('Content')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = models.Manager()

    
    def get_discount_price(self):
        if self.percent:
            return format_html(f'<span class="price">&#8358;{self.discount_prize()} </span>')
        else:
            return ''

    def get_square_label(self):
        if self.percent:
            return format_html(f'<span class="label-sale">-{self.percent}%</span>')       
        else:
            return ''

    def circle_label(self):
        if self.percent:
            return format_html(f'<span class="product-item-label label-price">{self.percent}% <span>off</span></span>')
        else:
            return ''

    def check_availability(self):
        if self.in_stock == True:
            return 'In Stock'
        else:
            return 'Out Of Stock'
    @property
    def get_price(self):
        format_number = "{:,}".format(self.price)
        if self.percent:
            return format_html(f'<span class="old-price">&#8358;{format_number} </span>')
        else:
            return format_html(f'<span class="price">&#8358;{format_number} </span>')

    
    
    class Meta:
        verbose_name_plural='3. Products'
        ordering = ('-created',)
    
    
    def discount_prize(self):
        if self.percent is not None:
            dis = self.price - self.price * self.percent/100
            format_number = "{:,}".format(dis)
            return format_number

    def display_whatsapp(self):
        whatsapp = settings.WHATSAPP_NUMBER
        message = 'https://wa.me/'+whatsapp+'?text='
        message += 'I am Interested In Buying This Product '
        message += '*Name:* '+self.title+' '
        message += '*Prize:* '+str(self.price)+' '
        return message

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
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural='4. About'

class Banner(models.Model):
    slide_img = CloudinaryField('Slide Image', help_text='Upload A Banner of 870px X 530px',  null=True, blank=True)
    slide_content1 = models.TextField(blank=True, null=True)
    slide_content2 = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.slide_content1[:5]
    
    def post_img(self):
        if self.slide_img:
          return self.slide_img.url

    class Meta():
        verbose_name_plural = 'Home Slider'

class HomeTopBanner(models.Model):
    banner = CloudinaryField(help_text='Upload A Banner Of 870px X 200px',)
    link = models.URLField(null=True, blank=True)
   

    class Meta():
        verbose_name_plural = 'Home Top Banner'

    def get_banner(self):
        if self.banner:
            return self.banner.url
    
    def get_link(self):
        if self.link:
            return self.link
        else:
            return '#'
    
    def __str__(self):
        return 'Home Banner'

class HomeSideBanner(models.Model):
    banner = CloudinaryField(help_text='Upload A Banner of 270px X 285px')
    link = models.URLField(null=True, blank=True)

    class Meta():
        verbose_name_plural = 'Home Side Banner'

    def get_banner(self):
        if self.banner:
            return self.banner.url

    def get_link(self):
        if self.link:
            return self.link
        else:
            return '#'
    
    def __str__(self):
        return 'Home Side Banner'

class HomeTwoSideBanner(models.Model):
    banner = CloudinaryField(help_text='Upload A Banner of 570px X 200px',)
    link = models.URLField(null=True, blank=True)
    

    class Meta():
        verbose_name_plural = 'Home Two SideBanner'

    def get_banner(self):
        if self.banner:
            return self.banner.url

    def get_link(self):
        if self.link:
            return self.link
        else:
            return '#'
    
    
    def __str__(self):
        return 'Home Banner'


class Pages(models.Model):
    page_title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = HTMLField('Content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} {self.page_title}'

    class Meta():
        verbose_name_plural = 'Pages'

    def get_absolute_url(self):
        return reverse('single_page', kwargs={'slug':self.slug})

class ContactInfo(models.Model):
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    email1 = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    phone1 = models.CharField(max_length=16, null=True, blank=True)
    phone2 = models.CharField(max_length=16, null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    class Meta():
        verbose_name_plural = 'Contact Info'
    
    
    def __str__(self):
        return 'Contact Information and Social Media Links'


