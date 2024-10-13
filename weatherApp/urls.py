from django.urls import path
from . import views  # Only this is needed since views.py is in the same directory

urlpatterns = [
    path('', views.index, name='index'),
]

