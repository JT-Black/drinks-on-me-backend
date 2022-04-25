from rest_framework import status  # gives list of possible response codes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
# This imports rest_framework's APIView that we'll use to extend to our custom view
from rest_framework.views import APIView
# Response gives us a way of sending a HTTP response to the user making the request, passing back data and other information
from rest_framework.response import Response
# Import this when adding error handling, provides a default response when data is not found
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import *

# list generic view


class UserList(ListCreateAPIView):

    # Handles all drinks
    queryset = AppUser.objects.all()

    # Choose serializer to use
    serializer_class = UserSerializer


# update or delete generic view
class UserUpdateDestroy(RetrieveUpdateDestroyAPIView):

    # Handles all books
    queryset = AppUser.objects.all()

    # Choose serializer to use
    serializer_class = UserSerializer


# get by ID generic view
class UserDetail(RetrieveAPIView):

    # Handles all books
    queryset = AppUser.objects.all()

    # Choose serializer to use
    serializer_class = UserSerializer

# add money class based view


class TopUp(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.user.id
        user = AppUser.objects.get(pk=user_id)
        amount = request.data["topup_amount"]
        print(f'User : {user}')
        print(f'Amount : {amount}')

        user.balance += amount

        print(f'User : {user}')

        return Response(status=200)
