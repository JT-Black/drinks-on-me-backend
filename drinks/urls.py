from django.urls import path
from .views import *

urlpatterns = [

  # Generic views for drinks

    path('', DrinkList.as_view()),
    path('<int:pk>/', DrinkUpdateDestroy.as_view()),
    path('detail/<int:pk>/', DrinkDetail.as_view()),
    path('pubdrinks/<int:pk>/', DrinksForPub.as_view()),  
]
