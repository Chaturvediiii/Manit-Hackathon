from django.urls import path,include
from . import views

urlpatterns = [
    path('panel/',views.get_pickuprequest,name='admin_panel'),

]
