 
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

 