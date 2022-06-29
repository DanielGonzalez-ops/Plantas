from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializers import ProductoSerializer, UsuarioSerializer
from app.models import Producto as ProductoModel
from app.models import Usuario as UsuarioModel

# Create your views here.
@permission_classes((permissions.AllowAny,))
@csrf_exempt
@api_view(['GET', 'POST'])
def Producto(request):

    if request.method == 'GET':
        producto = ProductoModel.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
@permission_classes((permissions.AllowAny,))
@csrf_exempt
@api_view(['GET', 'POST'])
def Usuario(request):

    if request.method == 'GET':
        usuario = UsuarioModel.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
