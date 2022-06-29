from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Usuario
from .forms import ProductoForm, UsuarioForm

# Create your views here.
def agregar(request): 
    data = {
         'form': ProductoForm()
    }         
    if request.method == 'POST':
        formulario = ProductoForm(data= request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Producto guardado"                                                
    return render(request, 'agregar.html', data)

def modificar(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="gestion")
        data["form"]=formulario
            
    return render(request,'modificar.html',data)  

def eliminar (request,id):
    producto= get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="gestion")      

def gestion(request):
    productos = Producto.objects.all() # devuelve todos los elementos guardados en la base de datos
    data={
        'productos': productos

    }
    return render(request, 'gestion.html',data )    

def menu(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'menu.html', data)

def base(request):
    return render(request, 'base.html', ) 

def registrousuario(request):
    data = {
         'form': UsuarioForm()
    }         
    if request.method == 'POST':
        formulario = UsuarioForm(data= request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Usuario guardado"                            
    return render(request, 'registrousuario.html',data ) 