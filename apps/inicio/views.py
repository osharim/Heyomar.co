<<<<<<< HEAD
 #encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from handlers.models import viewer
from helpers.core import get_client_ip
import datetime
from django.utils import timezone
import datetime


def aboutme_view(request):
 
	date =  timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())


 	viewer.objects.create( zone = 1 ,ip = get_client_ip(request ) , date = date) 
 
	ctx = {

			'aboutme_is_active' : True ,

		  }
 

	return render_to_response('inicio/inicio.html',ctx,  context_instance = RequestContext(request)  )


=======
#encoding:utf-8
from django.shortcuts import render_to_response
from django.core.serializers.json import DjangoJSONEncoder
from django.template import RequestContext
from django.http import HttpResponse , HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.contrib.auth.models import User
import datetime
from apps.inicio.models import Free , Code
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


def inicio_view(request):
	
 
	#data_category =  [ { "url" : " " , "name" : "Bienvenido" }]


	ctx = {'inicio_active' : True ,

			'requiere_select_project' : True , 

			}
 	
	
	return render_to_response('inicio/inicio.html',ctx,  context_instance = RequestContext(request)  )

#*****************************************************************************************************
 
	#*****************************************************************************************************
	#*****************************************************************************************************
	#*****************************************************************************************************
	#*****************************************************************************************************
	
def init_free_account_view(request , url ):

	url_generated = url


 
 	free_account_init_code = Free.objects.filter(url = url_generated )

 	if len(free_account_init_code) > 0 :

 		ctx = {

				'init_code' : 	free_account_init_code[0].code.code_txt ,

				'protection' : 	free_account_init_code[0].code.protection ,

				'url_generated' : url_generated ,

				'id_editor' : free_account_init_code[0].code.id , 

				'requiere_select_project' : False , 

				'viewer' :True 

		}


		return render_to_response('inicio/inicio.html' , ctx,  context_instance = RequestContext(request)  )

	else:


 

		free_account_init_code = Code.objects.create(code_txt='init project..aa' ,protection = False)
 
		free_account = Free.objects.create(url = url_generated , date = datetime.date.today() , code = free_account_init_code )
 


		ctx = {

				'init_code' : 	free_account_init_code.code_txt ,

				'protection' : 	free_account_init_code.protection ,

				'id_editor' : free_account_init_code.code.id , 

				'url_generated' : url_generated ,

				'coder' : True ,

		}


 		return render_to_response('inicio/inicio.html' , ctx,  context_instance = RequestContext(request)  )


#*****************************************************************************************************
 

@csrf_exempt
def upadte_code(request):


	post_parameter =  simplejson.loads(request.body)


	id_code = post_parameter["id"]

	code_Text =  post_parameter["code"]


	if request.is_ajax():

		
		if code_Text == False : # si solo queremos ver lo nuevo entonces 

			get_data_free_account =  Code.objects.filter(id = id_code )

		else: # si queremos actualizar los datos entonces .. 

			Code.objects.filter(id = id_code ).update(code_txt = code_Text)
			get_data_free_account =  Code.objects.filter(id = id_code )


		


 		json_values_query = serializers.serialize("json", get_data_free_account )
					
		return HttpResponse(  json_values_query , mimetype="application/json" )



	return HttpResponse(  False  , mimetype="application/json" )

 	 
>>>>>>> 96e61d3632b168c9e3ce901fa7154a12e754c9a7
