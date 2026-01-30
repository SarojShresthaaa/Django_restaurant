from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<int:id>/', CategoryDetails.as_view()),
    path('food/', FoodView.as_view()),
]