
from django.db import models
# sudo apt-get install python-mysqldb install on linux
 

class viewer(models.Model):
    id_viewer = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add = True)
    zone = models.IntegerField()
   
    class Meta:
        db_table = u'viewer'
 

    #def save(self,*args,**kwargs):
#
 #       self.date = timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())
#
 #       print timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())
#
 #       super(viewer,self).save(*args,**kwargs)


 