 #encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from helpers.core import get_client_ip




def skills_view(request):
 
  	viewer.objects.create( zone = 2 ,ip = get_client_ip(request ) ) 

	ctx = {

			'skills_is_active' : True ,

		  }
 

	return render_to_response('inicio/skills.html',ctx,  context_instance = RequestContext(request)  )


