from rest_framework import status # gives list of possible response codes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView # This imports rest_framework's APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a HTTP response to the user making the request, passing back data and other information
from rest_framework.exceptions import NotFound # Import this when adding error handling, provides a default response when data is not found
from .models import * 
from .serializers import * 

# list generic view
class DrinkList(ListCreateAPIView):

    # Handles all drinks
    queryset = Drink.objects.all()

    # Choose serializer to use
    serializer_class = DrinkSerializer


# update or delete generic view
class DrinkUpdateDestroy(RetrieveUpdateDestroyAPIView):

    # Handles all books
    queryset = Drink.objects.all()

    # Choose serializer to use
    serializer_class = DrinkSerializer


# get by ID generic view
class DrinkDetail(RetrieveAPIView):

    # Handles all books
    queryset = Drink.objects.all()

    # Choose serializer to use
    serializer_class = DrinkSerializer


class DrinksForPub(APIView):

    # Get Author by ID - pk is the primary key, passed through our <int:pk> route in urls.py
    def get(self, request, pk):
         # Call the get_author function which will either get the author or raise a HTTP 404 status code response if not present
        drinks = Drink.objects.filter(pub_id=pk)

        # Create a new serializer with the current author data - we're only returning one author so we don't need the many=True flag
        serialized_drinks = DrinkSerializer(drinks, many=True)

         # Return the serialized author data and a HTTP 200 response
        return Response(data=serialized_drinks.data, status=status.HTTP_200_OK)

