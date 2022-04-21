from django.db import models
from drinks.models import Drink
from users.models import User
from pubs.models import Pub


# Create your models here.

class Purchase(models.Model):
    drink = models.ForeignKey(Drink, related_name='purchases', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='purchases',on_delete=models.PROTECT)
    pub = models.ForeignKey(Pub, related_name='purchases',on_delete=models.PROTECT)



    def __str__(self):
        return f'drink: {self.drink}, user: {self.user}, pub: {self.pub}'