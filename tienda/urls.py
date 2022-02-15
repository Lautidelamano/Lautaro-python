from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar', views.agregar, name='agregar'),
    path('eliminar/<str:productos_id>', views.eliminar, name='eliminar'),
]
