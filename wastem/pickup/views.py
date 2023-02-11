from twilio.rest import Client
from django.shortcuts import render, redirect , HttpResponse
from .models import Location, PickupRequest
from .forms import PickupRequestForm

def send_sms(request):
    client = Client('AC916570d285355980fa8406cba9c38f42','14eaf82efb0c8b93d308bebdf9147698')
    message = client.messages.create(
        to='+918719062445',
        from_=+12173878678,
        body='Your pickup has been scheduled!'
    )
    return HttpResponse('SMS sent!')

def create_pickup_request(request):
    if request.method == 'POST':
        form = PickupRequestForm(request.POST)
        if form.is_valid():
            pickup_request = form.save()
            send_sms(request)
            return redirect('confirmation.html', pickup_request.id)
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




# def type(request):
#     if request.method == 'POST':
#         form = type(request.POST)
#         if form.is_valid():
#             type = form.save()
#             return redirect('pickup/create_request.html', {'form': form})
#         else:
#             form = type()
#             return redirect('user/profile.html', {'form': form})


