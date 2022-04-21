from django.urls import path
from .views import *

urlpatterns = [

  # Generic views for drinks

    path('', TransferList.as_view()),
    path('detail/<int:pk>/', TransferDetail.as_view()),  
    path('transfer/', Transfer.as_view()),
]
