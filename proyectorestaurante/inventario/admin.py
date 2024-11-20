from django.contrib import admin
from .models import Producto, Categoria
# Register your models here.

admin.site.register(Categoria)

class ProductoAdmin(admin.ModelAdmin): 
    list_display = ('nombre', 'cantidad', 'categoria')
    
admin.site.register(Producto, ProductoAdmin)    