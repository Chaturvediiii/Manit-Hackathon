from django.http import JsonResponse
from pickup.models import PickupRequest

def get_pickuprequest(request):
    PickupRequest_list = []
    pickuprequest = PickupRequest.objects.all()
    for PickupRequest in PickupRequest:
        PickupRequest_list.append({
            'Location': PickupRequest.location,
            'status': PickupRequest.status,
            'description': PickupRequest.description,
            'phone_number': PickupRequest.phone_number
        })
    return JsonResponse({'PickupRequest': PickupRequest_list})