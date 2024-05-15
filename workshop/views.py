from django.shortcuts import render
from .models import Service, Master, Order

def service_list(request):
    services = Service.objects.all()
    return render(request, 'workshop/service_list.html', {'services': services})

def master_list(request):
    masters = Master.objects.all()
    return render(request, 'master_list.html', {'masters': masters})

def create_order(request):
    if request.method == 'POST':
        car_model = request.POST['car_model']
        service_id = request.POST['service']
        master_id = request.POST['master']
        service = Service.objects.get(pk=service_id)
        master = Master.objects.get(pk=master_id)
        client_id = request.POST['client_id']
        total_price = service.price
        order = Order.objects.create(car_model=car_model, service=service, master=master, total_price=total_price)
        return render(request, 'order_confirmation.html', {'order': order})
    else:
        services = Service.objects.all()
        masters = Master.objects.all()
        return render(request, 'create_order.html', {'services': services, 'masters': masters})
