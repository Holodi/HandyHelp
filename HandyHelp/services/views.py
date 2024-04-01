from django.shortcuts import render, redirect, get_object_or_404

from .forms import ServiceForm
from .models import Service


def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.created_by = request.user
            service.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/add_service.html', {'form': form})

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'services/service_detail.html', {'service': service})

def edit_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_detail', service_id=service_id)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/edit_service.html', {'form': form, 'service': service})

def delete_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'services/delete_service_confirm.html', {'service': service})
