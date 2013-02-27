#encoding:utf-8
from django.conf.urls.defaults import patterns,url

#creamos nueva rama de urls

urlpatterns = patterns('apps.skills.views',  #Init View

			url(r'^skills$' ,   'skills_view' ,  name = 'vista_skills') ,  

			)