from django.urls import path 
from .views import post_list_create

urlpatterns = [
    
    path('list/',post_list_create,name='list')
]
