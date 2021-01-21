from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50, blank= True)
    country = models.CharField(max_length=50,blank=True)
    address = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=50,blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.user.username}'
