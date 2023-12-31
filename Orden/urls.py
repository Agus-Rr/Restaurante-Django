from django.urls import path
from . import views

urlpatterns = [
    path('homeOrdenes', views.ordenHome, name='homeOrdenes'),
    path('ordenNueva', views.ordenNueva, name='ordenNueva'),
    path('listaOrdenes', views.listaOrdenes, name='listaOrdenes'),
    path('editarOrden/<int:id>', views.editarOrden, name='editarOrden'),
    path('borrarOrden/<int:id>', views.borrarOrden, name='borrarOrden'),
    path('ordenEstado/<int:id>', views.estadoOrden, name='ordenEstado')
]