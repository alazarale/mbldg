from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'^home/$', views.home , name='home'),
    url(r'^rent/$', views.rental , name='rental'),
    url(r'^rent/success$', views.registered , name='registered'),
    url(r'^product/$', views.product, name='product'),
    url(r'^product/building/$', views.product_building, name='product_building'),
    url(r'^product/poultry$', views.product_poultry, name='product_poultry'),
    url(r'^product/dairy-farm$', views.product_dairy_farm, name='product_dairy_farm'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^service/$', views.service, name='service'),
    url(r'^news/$', views.news, name='news'),
    url(r'^developer/$', views.developer, name='developer'),
    url(r'^about/$', views.about, name='about'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^gallery/building/$', views.building, name='building'),
    url(r'^gallery/poultry/$', views.poultry, name='poultry'),
    url(r'^gallery/dairy_farm/$', views.dairy_farm, name='dairy_farm'),
    url(r'^gallery/farm/$', views.farm, name='farm'),
    url(r'^news/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.detail, name='detail'),
    url(r'^product/(?P<month>\d{2})/(?P<day>\d{2})/(?P<name>[-\w]+)/$', views.description, name='description')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)