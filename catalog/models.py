from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class UserInfo(models.Model):
    
    phone = models.CharField(max_length=20)
    idNumber = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    designation = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    
    user_Id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="detail")
    
    def __str__(self):
        return self.idNumber
    
    
