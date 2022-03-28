from django.db import models

# Create your models here.
class UserRegister(models.Model):
    
    username = models.CharField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length = 22)    