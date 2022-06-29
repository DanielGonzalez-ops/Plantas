from django.contrib import admin
from .models import Categoria, Marca, TipoPago,Usuario,Producto,TipoUsuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario','nombre','apellido','rut','dvRut','telefono','correo','contraseña','contraseña2','nacimiento']
    list_filter  = ['rut']
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','codBarra','descripcion','precioCosto','precioVenta','marca','categoria','imagen']
    list_filter  = ['codBarra']
    
class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_filter  = ['nombre', 'activo']

class TipoPagoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_filter  = ['nombre', 'activo']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_filter  = ['nombre', 'activo']

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_filter  = ['nombre', 'activo']


# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(TipoPago, TipoPagoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
