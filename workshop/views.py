from django.shortcuts import render,  get_object_or_404
from .models import Service, Master, Order

def service_list(request):
    services = Service.objects.all()
    return render(request, 'workshop/service_list.html', {'services': services})

def master_list(request, service_id=None):
    masters = Master.objects.all()
    selected_service = None
    if service_id:
        selected_service = get_object_or_404(Service, id=service_id)
    return render(request, 'workshop/master_list.html', {'masters': masters, 'selected_service': selected_service})




def create_order(request):
    master_id = request.GET.get('master_id')
    service_id = request.GET.get('service_id')

    master = get_object_or_404(Master, id=master_id)
    service = get_object_or_404(Service, id=service_id)

   
    car_model = "Toyota Camry"  
    hours_worked = 5  
    hourly_rate = master.price
    service_cost = service.price
    total_price = (hourly_rate * hours_worked) + service_cost

    order = {
        'car_model': car_model,
        'service': service,
        'master': master,
        'hours_worked': hours_worked,
        'hourly_rate': hourly_rate,
        'service_cost': service_cost,
        'total_price': total_price
    }

    context = {
        'order': order
    }
    return render(request, 'workshop/create_order.html', context)
