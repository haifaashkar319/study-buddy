from django.db import models

# Create your models here.
class user (models.Model):
    
    email =models.CharField(max_length=200, default="none")
    password = models.CharField(max_length=255, default="null")

    
    class Meta:
         db_table = 'sign_up_pages_user'