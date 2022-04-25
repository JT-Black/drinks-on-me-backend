from rest_framework import status # gives list of possible response codes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView # This imports rest_framework's APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a HTTP response to the user making the request, passing back data and other information
from rest_framework.exceptions import NotFound # Import this when adding error handling, provides a default response when data is not found
from .models import * 
from .serializers import * 

# list generic view
class PurchaseList(ListCreateAPIView):

    # Handles all drinks
    queryset = Purchase.objects.all()

    # Choose serializer to use
    serializer_class = PurchaseSerializer


# get by ID generic view
class PurchaseDetail(RetrieveAPIView):

    # Handles all books
    queryset = Purchase.objects.all()

    # Choose serializer to use
    serializer_class = PurchaseSerializer


# class based purchase view
class Purchase(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    user = AppUser.objects.get(pk=request.data["user_id"])
    pub = Pub.objects.get(pk=request.data["pub_id"])
    purchased_drink = Drink.objects.get(pk=request.data["drink_id"])
    purchase_amount = purchased_drink.price
    
    print(f'user :{user.username}')
    print(f'purchased drink:{purchased_drink}')
    print(f'pub :{pub.pubname}')

    if user.balance < purchase_amount:
      return Response(status=402, data='insufficient balance')
    else:
      user.balance -= purchase_amount
      pub.balance += purchase_amount 
      user.save()
      pub.save()
      print(f'user : {user}')
      print(f'pub : {pub}')

      return Response(status=200)

