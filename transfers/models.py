from django.db import models
from drinks.models import Drink
from users.models import AppUser


# Create your models here.

class Transfer(models.Model):
    message = models.CharField(max_length=400)
    amount = models.PositiveSmallIntegerField(null=True)
    send_date = models.DateField(null=True)
    sender = models.ForeignKey(AppUser, related_name='sent_transfers', null=True, on_delete=models.PROTECT )
    receiver = models.ForeignKey(AppUser, related_name='recd_transfers', null=True, on_delete=models.PROTECT)
    

    def __str__(self):
        return f'message: {self.message}, amount: {self.amount}, receiver: {self.receiver}, sender: {self.sender}'