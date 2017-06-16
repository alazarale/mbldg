from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='image/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('agri:detail', args=[
            self.created.year,
            self.created.strftime('%m'),
            self.created.strftime('%d'),
            self.slug,
        ])

class Contact(models.Model):
    name = models.CharField(_('name'), max_length=120)
    email = models.EmailField(_('email'))
    message = models.TextField(_('message'))
    sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent']

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='post_commented')
    name = models.CharField(_('name'),max_length=120)
    email = models.EmailField(_('email'))
    message = models.TextField(_('message'))
    commented = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.message

class Product(models.Model):
    STATUS = (('publish', 'Publish'), ('cancel', 'Cancel'))
    CHOICE = (
        ('Building', 'building'),
        ('Dairy farm', 'dairy farm'),
        ('Poultry', 'poultry')
    )

    catagory = models.CharField(max_length=50, choices=CHOICE, default='agri')
    name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='product/image/')
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    slug = models.SlugField()
    status = models.CharField(max_length=7, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('agri:description', args=[
            self.created.strftime('%m'),
            self.created.strftime('%d'),
            self.slug,
        ])

class Photo(models.Model):
    CHOICE = (
        ('Commercial building', 'commercial_building'),
        ('Dairy farm', 'dairy_farm'),
        ('Farm', 'farm'),
        ('Poultry', 'poultry')
           )
    category = models.CharField(max_length=30, choices=CHOICE)
    description = models.CharField(max_length=25)
    image = models.ImageField(upload_to='gallery/image/%Y/%m')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.description

class RentalRegistraion(models.Model):
    FLOOR = (
        ('Under Ground FLoor', 'under_ground_floor'),
        ('Ground Floor', 'ground_floor'),
        ('First Floor', 'first_floor'),
        ('Second Floor', 'second_floor'),
        ('3rd Floor', '3rd_floor'),
        ('Top Floor', 'top_floor')
        )
    r_t = (
        ('Person', 'person'),
        ('Organization', 'organization')
    )


    name = models.CharField(max_length=100)
    rental_type = models.CharField(max_length=20,choices=r_t)
    region = models.CharField(max_length=30)
    zone = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    kebele = models.CharField(max_length=30, blank=True)
    phone_no_1 = models.CharField(max_length=10)
    phone_no_2 = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    floor = models.CharField(max_length=20, choices=FLOOR)
    business_type = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

