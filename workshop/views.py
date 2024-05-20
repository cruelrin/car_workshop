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
    if request.method == 'POST':
        car_model = request.POST['car_model']
        service_id = request.POST['service']
        master_id = request.POST['master']
        service = get_object_or_404(Service, pk=service_id)
        master = get_object_or_404(Master, pk=master_id)
        hours_worked = int(request.POST.get('hours_worked', 5))  # Default to 5 hours if not provided
        total_price = hours_worked * master.price
        order = Order.objects.create(
            car_model=car_model,
            service=service,
            master=master,
            hours_worked=hours_worked,
            total_price=total_price
        )
        return render(request, 'workshop/create_order.html', {'order': order})
    else:
        master_id = request.GET.get('master_id')
        service_id = request.GET.get('service_id')
        master = get_object_or_404(Master, id=master_id)
        service = get_object_or_404(Service, id=service_id)
        return render(request, 'workshop/create_order.html', {'master': master, 'service': service})
