from django.urls import path
from .views import *

urlpatterns = [

  # Generic views for drinks

    path('', PurchaseList.as_view()),
    path('detail/<int:pk>/', PurchaseDetail.as_view()), 
    path('purchase/',Purchase.as_view()),   
]
