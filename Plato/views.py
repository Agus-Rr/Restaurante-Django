from django.shortcuts import render, redirect
from .forms import platoForm
from .models import Plato

# Create your views here.

def platoHome(request):
    return render(request, 'Plato/homePlatos.html')

def platoNuevo(request):
    formNuevo = platoForm

    contexto = {
        'form': formNuevo,
        'mensaje':'Crear Plato'
    }

    if request.method == 'POST':
        formPOST = platoForm(request.POST)

        if formPOST.is_valid():
            formPOST.save()
            return redirect('listaPlatos')
        else:
            contexto['mensaje']+='Error en el formulario'
            contexto['form'] = formPOST
    else:
        return render(request, 'Plato/formPlato.html', contexto)
    
def listaPlatos(request):
    platos = Plato.objects.all()

    contexto = {
        'titulo':'Lista de Platos',
        'platos':platos
    }

    return render(request, 'Plato/listaPlatos.html', contexto)

def editarPlato(request, id):
    platoEditar = Plato.objects.get(pk=id)

    if request.method == 'GET':
        formEditar = platoForm(instance=platoEditar)

        contextoGet = {
            'form' : formEditar,
            'mensaje' : 'Editar plato'
        }

        return render(request, 'Plato/formPlato.html', contextoGet)
    
    else:
        formGuardar = platoForm(request.POST, instance=platoEditar)

        if formGuardar.is_valid():
            formGuardar.save()
            return redirect('listaPlatos')
        else:
            return render(request, 'Plato/formPlato.html',
            {'form':formEditar, 'mensaje':'Error - Editar plato'})
        
def borrarPlato(request, id):
    mesaBorrar = Plato.objects.get(pk=id)
    mesaBorrar.delete()
    return redirect('listaPlatos')