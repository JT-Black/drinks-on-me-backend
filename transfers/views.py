from rest_framework import status # gives list of possible response codes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView # This imports rest_framework's APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a HTTP response to the user making the request, passing back data and other information
from rest_framework.exceptions import NotFound # Import this when adding error handling, provides a default response when data is not found
from .models import * 
from .serializers import * 

# list generic view
class TransferList(ListCreateAPIView):

    # Handles all drinks
    queryset = Transfer.objects.all()

    # Choose serializer to use
    serializer_class = TransferSerializer


# get by ID generic view
class TransferDetail(RetrieveAPIView):

    # Handles all books
    queryset = Transfer.objects.all()

    # Choose serializer to use
    serializer_class = TransferSerializer

# class based views

class Transfer(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    sending_user_id = request.user.id
    receiving_user_id = request.data["receiver_id"]
    transfer_amount = request.data["amount"]
    transfer_message = request.data["message"]
    print(f'sender id:{sending_user_id}')
    print(f'receiver id:{receiving_user_id}')
    sending_user = AppUser.objects.get(pk=sending_user_id)
    receiving_user = AppUser.objects.get(pk=receiving_user_id)
    print(f'sender :{sending_user}')
    print(f'receiver :{receiving_user}')
    # if int(sending_user.balance) < transfer_amount:
    #   return Response(status=402, data='insufficient balance')
    # else:
    sending_user.balance -= transfer_amount
    receiving_user.balance += transfer_amount 
    sending_user.save()
    receiving_user.save()
    print(f'sender :{sending_user}')
    print(f'receiver :{receiving_user}')


    return Response(status=200)

      