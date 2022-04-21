from django.urls import path
from .views import *

urlpatterns = [

  # Generic views for drinks

    path('', PubList.as_view()),
    path('<int:pk>/', PubUpdateDestroy.as_view()),
    path('detail/<int:pk>/', PubDetail.as_view()),
]
