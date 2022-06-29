from app.models import Producto, Usuario
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields = "__all__"