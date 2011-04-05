from django.conf.urls.defaults import patterns, include, url

# Importing staticfiles_urlpatterns 
# - http://docs.djangoproject.com/en/1.3/howto/static-files/#staticfiles-development
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$',             'direct_to_template', {'template': 'base.html'}),
    # (r'^foo/(?P<id>\d+)/$', 'direct_to_template', {'template': 'foo_detail.html'}),
)

# Importing staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()