 #encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from handlers.models import viewer
from helpers.core import get_client_ip
import datetime
from django.utils import timezone
import datetime
from django.utils.timezone import utc
 

def aboutme_view(request):
 
	date =  timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())

 

	print date 

 	viewer.objects.create( zone = 1 ,ip = get_client_ip(request ) , date = date) 
 
	ctx = {

			'aboutme_is_active' : True ,

		  }
 

	return render_to_response('inicio/inicio.html',ctx,  context_instance = RequestContext(request)  )


