<<<<<<< HEAD
from django.db import models

# Create your models here.
=======
 
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Code(models.Model):
    
    code_txt = models.TextField(db_column='Code_txt') # Field name made lowercase.
    protection = models.BooleanField()
    class Meta:
        db_table = u'Code'

class Free(models.Model):
  
    url = models.CharField(max_length=150)
    date = models.DateField()
    code = models.ForeignKey(Code)
    class Meta:
        db_table = u'free'

>>>>>>> 96e61d3632b168c9e3ce901fa7154a12e754c9a7
