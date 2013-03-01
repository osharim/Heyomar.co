import datetime
from django.db import models
# sudo apt-get install python-mysqldb install on linux
 

class viewer(models.Model):
    id_viewer = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=100)
    date = models.DateTimeField()
    zone = models.IntegerField()
   
    class Meta:
        db_table = u'viewer'
 

    def save(self,*args,**kwargs):

        self.date = datetime.datetime.now()

        super(viewer,self).save(*args,**kwargs)


 