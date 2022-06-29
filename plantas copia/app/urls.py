from django.urls import path
from .views import agregar, base, gestion, menu, registrousuario, modificar, eliminar

urlpatterns = [
    path('base/', base, name='base'),
    path('agregar/', agregar , name='agregar'),
    path('gestion/', gestion, name='gestion'),
    path('menu/', menu, name='menu'),
    path('registrousuario/', registrousuario, name='registrousuario'),
    path('modificar/<id>/', modificar, name='modificar'),
    path('eliminar/<id>/', eliminar, name='eliminar'),
    ]