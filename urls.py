from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'website/login.html'}),
    (r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'website/login.html'}),
    (r'^new/$', 'website.views.new'),
    (r'^search/(.*?)$', 'website.views.search'),
    (r'^view/(\d+)$', 'website.views.view'),
    (r'^export/$', 'website.views.export'),
    (r'^ramas/$', 'website.views.ramas'),
    (r'^$', 'website.views.index'),

    # Example:
    # (r'^census/', include('census.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
