#encoding:utf-8
from django.shortcuts import render_to_response
from django.core.serializers.json import DjangoJSONEncoder
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson

def init_view(request):
	
 
	#data_category =  [ { "url" : " " , "name" : "Bienvenido" }]


	ctx = {'inicio_active' : True ,


			}
 	
	
	return render_to_response('init/init.html',ctx,  context_instance = RequestContext(request)  )

