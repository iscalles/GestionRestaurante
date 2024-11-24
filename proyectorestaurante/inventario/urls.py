from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('actualizar-cantidad/<int:producto_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
]
