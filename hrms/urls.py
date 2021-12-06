from django.urls import path, include
from . import  views
from rest_framework import routers

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hrms/', include('hrms.urls', ) ),
    path('', views.index, name= 'home'),
    path('register/', views.registration, name= 'registration'),
    path('books/', views.books, name= 'books'),
    
]