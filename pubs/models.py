from django.db import models

# Create your models here.

class Pub(models.Model):

    pubname = models.CharField(max_length=100)
    balance = models.IntegerField(null=True)
    image = models.CharField(max_length=200)
    email = models.CharField(max_length=100)


    def __str__(self):
        return f'Pub : {self.pubname}, Balance : {self.balance}'