from django.urls import path
from .views import Producto, Usuario
urlpatterns = [
    path('apiProducto', Producto, name="apiProducto"),
    path('apiUsuario', Usuario, name="apiUsuario"),]