from django.urls import path,include
from . import views
from .  import *

urlpatterns = [
    path('home/',views.index,name='index'),
]