from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AppUser(AbstractUser):

    
    balance = models.IntegerField(null=False)
    image = models.CharField(max_length=200, null=True)
    


    def __str__(self):
        return f'{self.username}, Balance: £{self.balance}'