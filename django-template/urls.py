from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django-template.app.views.home', name='home'),
    url(r'^login/$', 'django-template.app.views.do_login', name='login'),
    url(r'^logout/$', 'django-template.app.views.do_logout', name='logout'),


    # url(r'^django-template/', include('django-template.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
