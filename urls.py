from django.conf.urls.defaults import patterns, include, url

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
    (r'^$', 'direct_to_template', {'template': 'base.html'}),
    # (r'^foo/(?P<id>\d+)/$', 'direct_to_template', {'template': 'foo_detail.html'}),
)

# Serving static/media files could be better with Django. Here's how to do it in the development server (and use href="{{ STATIC_URL }}css/mysite.css" in mysite/myproject/templates/base.html). In production I believe it will be controlled by a setting in mysite/myproject/etc/nginx.conf
# http://docs.djangoproject.com/en/dev/howto/static-files/#serving-static-files-in-development
from django.conf import settings

if settings.DEBUG :
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    )