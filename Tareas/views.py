from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import render


class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    

def home(request):
    return render(request, 'Hola.html') 