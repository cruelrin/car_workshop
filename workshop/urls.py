from django.urls import path
from .views import service_list, master_list, create_order

urlpatterns = [
    path('', service_list, name='service_list'),  
    path('masters/', master_list, name='master_list'),
    path('masters/<int:service_id>/', master_list, name='master_list_with_service'),
    path('create_order/', create_order, name='create_order'),
    path('create_order/<int:order_id>/', create_order, name='create_order_detail'),
]
