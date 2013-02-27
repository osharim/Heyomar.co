#encoding:utf-8
from django.conf.urls.defaults import patterns,url

#creamos nueva rama de urls

urlpatterns = patterns('apps.inicio.views',  #Init View

			url(r'^$' ,    'aboutme_view' ,  name = 'vista_aboutme') ,  

			)