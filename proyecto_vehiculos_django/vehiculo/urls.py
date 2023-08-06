from django.urls import path
from .views import indexView, addVehiculo, registro_view, login_view, listar_vehiculo

urlpatterns = [
    path('', indexView, name = 'index'),
    path('add/', addVehiculo, name = 'addvehiculo'),
    path('registro/', registro_view, name="registro"),
    path('login/', login_view, name='login'),
    path('listar/', listar_vehiculo, name = 'listar'),
]