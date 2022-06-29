from django.contrib import admin
from .models import Producto, Usuario

admin.site.register(Producto)
# Register your models here.
admin.site.register(Usuario)