from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class LibararyUser(AbstractUser):
    phone_number = models.CharField(max_length = 100,unique = True)
    libaray_name =  models.CharField(max_length=50,null=True, blank=True, unique=True)
    user_choies_type = [
        ('student','student'),
        ('librariyan','librariyan'),
        ('other','other')
    ]
    user_type =  models.CharField(
        max_length=15,
        choices=user_choies_type,
        default='other',
    )
   
    
