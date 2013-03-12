from django.conf.urls import patterns, include, url
from django.conf import settings
 


urlpatterns = patterns('',

    url(r'^' , include('apps.init.urls')) , # va a jalar las urls de nuestra aplicacion sucursales

	url(r'^' , include('apps.inicio.urls')) , # va a jalar las urls de nuestra aplicacion sucursales


    url(r'^' , include('apps.free.urls')) , # va a jalar las urls de nuestra aplicacion sucursales
    # Examples:
    # url(r'^$', 'codlr.views.home', name='home'),
    # url(r'^codlr/', include('codlr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    ) 
