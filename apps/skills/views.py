<<<<<<< HEAD
 #encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from apps.handler import app

def skills_view(request):
 
 
	ctx = {

			'skills_is_active' : True ,
			'VERSION' : app.VERSION,
		  }
 

	return render_to_response('inicio/skills.html',ctx,  context_instance = RequestContext(request)  )


