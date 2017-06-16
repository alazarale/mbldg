from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    # Examples:
    # url(r'^$', 'michael.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^', include('agri.urls', namespace='agri')),
    url(r'^rosetta/', include('rosetta.urls')),

)

urlpatterns += url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root', settings.STATIC_ROOT}
  ),