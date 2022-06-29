from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    nombre = models.TextField(max_length=200)
    codBarra = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=200)
    precioCosto = models.TextField(max_length=200)
    precioVenta = models.TextField(max_length=200)
    marca = models.TextField(max_length=200)
    categoria = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to="productos", null=True)

    def str(self):
        return self.codBarra

class Usuario(models.Model):
    usuario = models.TextField(max_length=100)
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    rut = models.TextField(max_length=100)
    dvRut = models.TextField(max_length=100)
    telefono = models.TextField(max_length=12) 
    contraseña = models.TextField(max_length=100)
    contraseña2 = models.TextField(max_length=100)
    correo = models.TextField(max_length=100)
    nacimiento = models.TextField(max_length=100)

    def str(self):
        return self.rut

class TipoUsuario(models.Model):
    nombre = models.TextField(max_length=100)
    activo = models.BooleanField()

    def str(self):
        return self.nombre

class TipoPago(models.Model):
    nombre = models.TextField(max_length=100)
    activo = models.BooleanField()

    def str(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.TextField(max_length=100)
    activo = models.BooleanField()

    def str(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.TextField(max_length=100)
    activo = models.BooleanField()

    def str(self):
        return self.nombre

