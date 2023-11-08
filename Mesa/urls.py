from django.urls import path
from . import views

urlpatterns = [
    path('homeMesa', views.mesaHome, name='homeMesa'),
    path('mesaNueva', views.mesaNueva, name='mesaNueva'),
    path('listaMesas', views.listaMesas, name='listaMesas'),
    path('editarMesa/<int:id>', views.editarMesa, name='editarMesa'),
    path('borrarMesa/<int:id>', views.borrarMesa, name='borrarMesa')
]