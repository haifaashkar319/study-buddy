from django.db import models

# Create your models here.
class feed (models.Model):
    
    Feed_Owner = models.IntegerField(max_length=255)
    Description = models.CharField(max_length=255,default="none")
    Knowledge = models.IntegerField(max_length=255)
    course= models.IntegerField(max_length=255)
    isDeleted=models.BooleanField(default=False)   

    class Meta:
        db_table = 'feedtable'                      

    


# class request(models.Model):
#     Requesting =models.IntegerField(max_length=255)
#     Owner= models.IntegerField(max_length=255)
#     Feed= models.IntegerField(max_length=255)
#     Course= models.IntegerField(max_length=255)
#     status= models.CharField(max_length=255)



#     class Meta:
#          db_table_new='requesttable'


