from django.shortcuts import render, redirect
from .models import Location, PickupRequest
from .forms import PickupRequestForm

def create_pickup_request(request):
    if request.method == 'POST':
        form = PickupRequestForm(request.POST)
        if form.is_valid():
            pickup_request = form.save()
            return redirect('pickup/confirmation.html', pickup_request.id)
    else:
        form = PickupRequestForm()
    return render(request, 'pickup/create_request.html', {'form': form})

def pickup_request_confirmation(request, pickup_request_id):
    pickup_request = PickupRequest.objects.get(id=pickup_request_id)
    return render(request, 'pickup/confirmation.html', {'pickup_request': pickup_request})

def view_pickup_requests(request):
    pickup_requests = PickupRequest.objects.all()
    return render(request, 'pickup/view_request.html', {'pickup_request': pickup_requests})

def location(request):
    if request.method == 'POST':
        form = Location(request.POST)
        if form.is_valid():
            Location = form.save()
            return redirect('pickup/create_request.html', {'form': form})
        else:
            form = Location()
            return redirect('user/profile.html', {'form': form})
