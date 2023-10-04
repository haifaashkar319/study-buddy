from django.db import models

# Create your models here.
class user (models.Model):
    
    First_Name =models.CharField(max_length=200, default="none")
    Last_Name = models.CharField(max_length=200, default="none")
    GPA = models.DecimalField(max_digits=3,decimal_places=2, default=0)
    Gender=models.TextField(default="none")
    Major= models.TextField (default="Majorless")
    email = models.TextField(default="null")
    password = models.CharField(max_length=255, default="null")  # Note: Password should be securely hashed and stored
    PhoneNumber= models.DecimalField(max_digits=65,decimal_places=0, default=0)
    #Photo
    class meta:
         db_table = 'sign_up_pages_user'
        
