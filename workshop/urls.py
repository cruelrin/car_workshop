from django.urls import path
from .views import service_list, master_list, create_order

urlpatterns = [
    path('', service_list, name='service_list'),  # URL pattern for the root URL
      # Keep the URL pattern for service list
    path('masters/', master_list, name='master_list'),
    path('create_order/', create_order, name='create_order'),
]
