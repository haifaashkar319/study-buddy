from django.db import models

# Create your models here.
class Request (models.Model):
    delete_accept_button = models.BooleanField(default=False)
    