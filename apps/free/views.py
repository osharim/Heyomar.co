#encoding:utf-8
from django.shortcuts import render_to_response
from django.core.serializers.json import DjangoJSONEncoder
from django.template import RequestContext
from django.http import HttpResponse , HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.contrib.auth.models import User

 

def free_acount_generate_url(request ):

	url_generated = User.objects.make_random_password()

	ctx = {'inicio_active' : True  
			 

			}
 	
 	return HttpResponseRedirect(reverse('init_free_account', args=[url_generated]))
	
 
 




 