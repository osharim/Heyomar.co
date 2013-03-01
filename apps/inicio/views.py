 #encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from handlers.models import viewer
from helpers.core import get_client_ip


def aboutme_view(request):
 
 	viewer.objects.create( zone = 1 ,ip = get_client_ip(request ) ) 
 
	ctx = {

			'aboutme_is_active' : True ,

		  }
 

	return render_to_response('inicio/inicio.html',ctx,  context_instance = RequestContext(request)  )


