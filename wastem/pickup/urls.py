from django.urls import path,include
from . import views
from .  import *

urlpatterns = [
    path('request/',views.create_pickup_request,name='create_request'),
    path('confirmation/',views.pickup_request_confirmation,name='cconfirm_request'),
    path('view/',views.view_pickup_requests,name='view_request'),
    # path('template/',views.template,name='template'),


]