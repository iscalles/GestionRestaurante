from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Categoria
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def home (request):
    producto = Producto.objects.all()
    return render(request, 'home.html', {'producto':producto})

@csrf_exempt
def actualizar_cantidad(request, producto_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        nueva_cantidad = data.get('cantidad')
        try:
            producto = Producto.objects.get(id=producto_id)
            producto.cantidad = nueva_cantidad
            producto.save()
            return JsonResponse({'success': True})
        except Producto.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Producto no encontrado'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})