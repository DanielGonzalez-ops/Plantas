from django import forms
from .models import Producto, Usuario

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    codBarra = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    precioCosto = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    precioVenta = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    marca = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    categoria = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    #imagen = forms.ImageField
    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    rut = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    dvRut = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    contraseña = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    contraseña2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    correo = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    nacimiento = forms.CharField(widget=forms.TextInput(attrs={"class": "form_control"}))
    
    class Meta:
        model = Usuario
        fields = '__all__'
