from django.urls import path 
from .views import post_list,post_create, post_get,post_update_delete

urlpatterns = [
    
    path('list/',post_list,name='list'),
    path('create/',post_create,name='create'),
    path('<str:slug>/detail/',post_get,name='detail'),
    path('<str:slug>/update/',post_update_delete,name='update'),
]
