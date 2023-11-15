from django.shortcuts import render, redirect
from .forms import mesaForm
from .models import Mesa
from Orden.models import Orden

# Create your views here.

def mesaHome(request):
    return render(request, 'Mesa/homeMesas.html')

def mesaNueva(request):
    formNuevo = mesaForm

    contexto = {
        'form': formNuevo,
        'mensaje':'Crear Mesa'
    }

    if request.method == 'POST':
        formPOST = mesaForm(request.POST)

        if formPOST.is_valid():
            formPOST.save()
            return redirect('listaMesas')
        else:
            contexto['mensaje']+='Error en el formulario'
            contexto['form'] = formPOST
    else:
        return render(request, 'Mesa/formMesa.html', contexto)
    
def listaMesas(request):
    mesas = Mesa.objects.filter(disponible=True)
    mesasOcupadas = Mesa.objects.filter(disponible=False)

    contexto = {
        'titulo':'Lista de Mesas',
        'mesas':mesas,
        'mesasOcupadas':mesasOcupadas
    }

    return render(request, 'Mesa/listaMesas.html', contexto)

def editarMesa(request, id):
    mesaEditar = Mesa.objects.get(pk=id)

    if request.method == 'GET':
        formEditar = mesaForm(instance=mesaEditar)

        contextoGet = {
            'form' : formEditar,
            'mensaje' : 'Editar mesa'
        }

        return render(request, 'Mesa/formMesa.html', contextoGet)
    
    else:
        formGuardar = mesaForm(request.POST, instance=mesaEditar)

        if formGuardar.is_valid():
            formGuardar.save()
            return redirect('listaMesas')
        else:
            return render(request, 'Mesa/formMesa.html',
            {'form':formEditar, 'mensaje':'Error - Editar mesa'})
        
def borrarMesa(request, id):
    mesaBorrar = Mesa.objects.get(pk=id)
    mesaBorrar.delete()
    return redirect('listaMesas')
