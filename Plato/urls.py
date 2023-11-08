from django.urls import path
from . import views

urlpatterns = [
    path('homePlatos', views.platoHome, name='homePlatos'),
    path('platoNuevo', views.platoNuevo, name='platoNuevo'),
    path('listaPlatos', views.listaPlatos, name='listaPlatos'),
    path('editarPlato/<int:id>', views.editarPlato, name='editarPlato'),
    path('borrarPlato/<int:id>', views.borrarPlato, name='borrarPlato')
]