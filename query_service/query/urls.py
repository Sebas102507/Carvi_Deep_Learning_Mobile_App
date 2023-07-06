from django.urls import path
from . import views

urlpatterns = [    
    path('getCarName/',views.getCarName),
]