from django.contrib import admin
from .models import Post, Contact, Comment, Product, Photo, RentalRegistraion
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.

class PostAdmin(MarkdownModelAdmin):
    list_display = ['title', 'photo', 'created', 'updated']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, PostAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'sent']

admin.site.register(Contact, ContactAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'commented']

admin.site.register(Comment, CommentAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)

class PhotosAdmin(admin.ModelAdmin):
    list_display = ['description', 'created', 'category']

admin.site.register(Photo, PhotosAdmin)

class RentalRegistraionAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_no_1', 'business_type']

admin.site.register(RentalRegistraion, RentalRegistraionAdmin)