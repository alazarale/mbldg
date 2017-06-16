from django.shortcuts import render, HttpResponseRedirect
from .models import Post, Product, Photo
from .forms import ContactForm, CommentForm, RentalRegistraionForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
# Create your views here.

def home(request):
    posts = Post.objects.filter(active=True)[:3]
    products = Product.objects.filter(status='publish')[:2]
    if request.POST:
        form_contact = ContactForm(data=request.POST)
        if form_contact.is_valid():
            cd = form_contact.cleaned_data
            form_contact.save()

    else:
        form_contact = ContactForm()
    return render(request, 'contents/home.html', {'posts':posts, 'status':'home', 'form_contact':form_contact, 'products': products})

def news(request):
    object_list = Post.objects.filter(active=True)
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'contents/news.html', {'posts': posts, 'status':'news', 'page':page})

def detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             created__year=year,
                             created__month=month,
                             created__day=day,
                             slug=post,
                             )
    posts = Post.objects.filter(active=True)[:3]
    comments = post.post_commented.all()


    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_form = comment_form.save(commit=False)
            new_form.post = post
            new_form.save()
    else:
        comment_form = CommentForm()

    return render(request, 'contents/detail.html', {'post': post, 'posts':posts, 'comment_form': comment_form, 'comments': comments})

def product(request):
    building = Product.objects.filter(catagory='Building').filter(status='publish')
    dairy_farm = Product.objects.filter(catagory='Dairy farm').filter(status='publish')
    poultry = Product.objects.filter(catagory='Poultry').filter(status='publish')
    return render(request, 'contents/product.html', {'building': building,'dairy_farm':dairy_farm, 'poultry':poultry, 'status':'product'})

def product_building(request):
    building = Product.objects.filter(catagory='Building').filter(status='publish')
    return render(request, 'contents/product_building.html',
                  {'building': building, 'status': 'product'})

def product_poultry(request):
    poultry = Product.objects.filter(catagory='Poultry').filter(status='publish')
    return render(request, 'contents/product_poultry.html',
                  {'poultry': poultry, 'status': 'product'})

def product_dairy_farm(request):
    dairy_farm = Product.objects.filter(catagory='Dairy farm').filter(status='publish')
    return render(request, 'contents/product_farm.html',
                  {'dairy_farm': dairy_farm, 'status': 'product'})

def description(request, month, day, name):
    product = get_object_or_404(Product,
                                created__month=month,
                                created__day = day,
                                slug=name,
    )

    return render(request, 'contents/description.html', {'product':product})

def contact(request):
    if request.POST:
        form_contact = ContactForm(data=request.POST)
        if form_contact.is_valid():
            cd = form_contact.cleaned_data
            form_contact.save()
            subject = 'Message from the site'
            message = "hello there"
            from_email = 'fordjangouse@gmail.com'
            to = ('fordjangouse@gmail.com',)
            send_mail(subject, message, from_email, to, fail_silently=False)
    else:
        form_contact = ContactForm()
    return render(request, 'contents/contact.html', {'status':'contact', 'form_contact': form_contact})

def service(request):
    return render(request, 'contents/service.html', {'status': 'service'})

def about(request):
    return render(request, 'contents/about.html', {'status': 'about'})

def gallery(request):
    building = Photo.objects.filter(category='Commercial building')[:8]
    poultry = Photo.objects.filter(category='Poultry')[:8]
    dairy_farm = Photo.objects.filter(category='Dairy farm')[:8]
    farm = Photo.objects.filter(category='Farm')[:3]
    print(building)
    print(building[0].image.url)
    return render(request,
                  'contents/gallery.html',
                  {'status': 'gallery',
                    'building':building,
                    'poultry': poultry,
                    'dairy_farm':dairy_farm,
                    'farm': farm,}
                  )

def building(request):
    building = Photo.objects.filter(category='Commercial building')
    return render(request, 'contents/building_gallery.html', {'building': building, 'status': 'gallery'})

def poultry(request):
    poultry = Photo.objects.filter(category='Poultry')
    return render(request, 'contents/poultry_gallery.html', {'poultry':poultry, 'status': 'gallery'})

def dairy_farm(request):
    dairy_farm = Photo.objects.filter(category='Dairy farm')
    return render(request, 'contents/dairy_farm_gallery.html', {'dairy_farm':dairy_farm, 'status': 'gallery'})

def farm(request):
    farm = Photo.objects.filter(category='Farm')
    return render(request, 'contents/farm_gallery.html', {'farm':farm, 'status': 'gallery'})

def developer(request):
    return render(request, 'contents/developer.html', {})

def rental(request):
    if request.POST:
        form_rental = RentalRegistraionForm(data=request.POST)
        if form_rental.is_valid():
            cd = form_rental.cleaned_data
            form_rental.save()
            return HttpResponseRedirect('success')

    else:
        form_rental = RentalRegistraionForm()
    return render(request, 'contents/rental.html', {'form_rental':form_rental})

def registered(request):
    return render(request, 'contents/registered.html')