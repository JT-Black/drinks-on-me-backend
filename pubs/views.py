from rest_framework import status # gives list of possible response codes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView # This imports rest_framework's APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a HTTP response to the user making the request, passing back data and other information
from rest_framework.exceptions import NotFound # Import this when adding error handling, provides a default response when data is not found
from .models import * 
from .serializers import * 

# list generic view
class PubList(ListCreateAPIView):

    # Handles all drinks
    queryset = Pub.objects.all()

    # Choose serializer to use
    serializer_class = PubSerializer


# update or delete generic view
class PubUpdateDestroy(RetrieveUpdateDestroyAPIView):

    # Handles all books
    queryset = Pub.objects.all()

    # Choose serializer to use
    serializer_class = PubSerializer


# get by ID generic view
class PubDetail(RetrieveAPIView):

    # Handles all books
    queryset = Pub.objects.all()

    # Choose serializer to use
    serializer_class = PubSerializer

