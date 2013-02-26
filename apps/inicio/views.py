 #encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
 
def inicio_view(request):
 
 
	ctx = {

			'aboutme_is_active' : True ,

		  }
 

	return render_to_response('inicio/inicio.html',ctx,  context_instance = RequestContext(request)  )


