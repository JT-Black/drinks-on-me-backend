from rest_framework import serializers
from .models import *

class PubSerializer(serializers.ModelSerializer):

  class Meta:
    model = Pub
    fields = ('__all__')