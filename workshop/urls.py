from django.urls import path
from .views import service_list, master_list, create_order
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', service_list, name='service_list'),  
    path('masters/', master_list, name='master_list'),
    path('create_order/', create_order, name='create_order'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
