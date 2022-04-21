from django.db import models
from pubs.models import Pub

# Create your models here.


class Drink(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField(default=1)
    pub = models.ForeignKey(Pub, related_name='pubs',on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}, £{self.price}, Pub: {self.pub.pubname}'