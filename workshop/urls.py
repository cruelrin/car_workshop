from django.urls import path
from .views import service_list, master_list, create_order

urlpatterns = [
    path('', service_list, name='service_list'),  
    path('masters/', master_list, name='master_list'),
    path('create_order/', create_order, name='create_order'),
    
]
