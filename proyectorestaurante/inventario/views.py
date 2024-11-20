from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Categoria
# Create your views here.
def home (request):
    producto = Producto.objects.all()
    return render(request, 'home.html', {'producto':producto})