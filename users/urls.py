from django.urls import path
from .views import *

urlpatterns = [

  # Generic views for drinks

    path('', UserList.as_view()),
    path('<int:pk>/', UserUpdateDestroy.as_view()),
    path('detail/<int:pk>/', UserDetail.as_view()),
    path('topup/',TopUp.as_view()),
]

