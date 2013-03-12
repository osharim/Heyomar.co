#encoding:utf-8
from django.conf.urls.defaults import patterns,url

 #creamos nueva rama de urls

urlpatterns = patterns('apps.inicio.views', #prefijos de la vista que queremos jalar archivo donde estamos jalando las vistas

			url(r'^$' ,    'inicio_view' ,  name = 'vista_inicio') ,  

			url(r'^(?P<url>.*)/$' ,    'init_free_account_view' , name="init_free_account") , 


			url(r'^update/$' ,    'upadte_code' ,  name = 'vista_update') ,  
 

			) #cerramos la creacion de las ramas


#Este codigo asocia URLs, como simples expresiones regulares, a la ubicacion de funciones Python ("vistas").
#Las expresiones regulares usan paréntesis para "capturar" valores de las URLs. Cuando un usuario solicita una página,
#Django pasa por cada patron, en orden, y se detiene en el primero que coincida con la URL solicitada. (Si ninguno coincide,
#Django llama una vista especial 404). Esto es increíblemente rápido, porque las expresiones regulares son compiladas cuando se carga el codigo.

#Una vez que una de las expresiones coincide, Django importa y llama la vista correspondiente, la cual es una simple función Python. 
#Cada vista recibe un objeto request -- que contiene la metadata de la peticion -- y los valores capturados en la expresión regular.

#Por ejemplo, si un usuario solicita la URL "/articles/2007/05/39323/", Django llamaria a la funcion
#                                           mysite.views.article_detail(request, '2007', '05', '39323').
#					    (r'^/articles/(\d{4})/(\d{2})/(\d+)/$', 'mysite.views.article_detail'),


#Contiene las rutas que están disponibles en el proyecto, manejado por URLConf, los detalles completos como siempre en
#la documentación oficial nos da mas detalles sobre las urls y Django. https://docs.djangoproject.com/en/dev/topics/http/urls/#topics-http-urls


#Para diseñar las URLs de la aplicación, se crea un módulo Python llamado URLconf: es como una tabla de contenidos para la aplicación que 
#contiene un mapeo simple entre patrones de URLs y funciones Python. Las URLconfs también sirven para desacoplar las URLs del código Python.
