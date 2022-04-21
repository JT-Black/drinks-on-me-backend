from rest_framework import serializers
from .models import *

class TransferSerializer(serializers.ModelSerializer):

  class Meta:
    model = Transfer
    fields = ('__all__')