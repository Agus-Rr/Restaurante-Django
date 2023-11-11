from django.shortcuts import render, redirect
from .forms import ordenForm
from .models import Orden
from Plato.models import Plato

# Create your views here.

def ordenHome(request):
    return render(request, 'Orden/homeOrdenes.html')

def ordenNueva(request):
    formNuevo = ordenForm

    contexto = {
        'form': formNuevo,
        'mensaje':'Crear Orden'
    }

    if request.method == 'POST':
        formPOST = ordenForm(request.POST)

        if formPOST.is_valid():
            print(request.POST)
            formPOST.save()
            return redirect('listaOrdenes')
        else:
            contexto['mensaje']+='Error en el formulario'
            contexto['form'] = formPOST
    else:
        return render(request, 'Orden/formOrden.html', contexto)
    
def listaOrdenes(request):
    ordenes = Orden.objects.filter(estado=False)
    ordenCompleto = Orden.objects.filter(estado=True)

    contexto = {
        'titulo':'Lista de Ordenes',
        'ordenes':ordenes,
        'ordenCompleto' :ordenCompleto,
    }

    return render(request, 'Orden/listaOrdenes.html', contexto)

def editarOrden(request, id):
    ordenEditar = Orden.objects.get(pk=id)

    if request.method == 'GET':
        formEditar = ordenForm(instance=ordenEditar)

        contextoGet = {
            'form' : formEditar,
            'mensaje' : 'Editar orden'
        }

        return render(request, 'Orden/formOrden.html', contextoGet)
    
    else:
        formGuardar = ordenForm(request.POST, instance=ordenEditar)

        if formGuardar.is_valid():
            formGuardar.save()
            return redirect('listaOrdenes')
        else:
            return render(request, 'Orden/formOrden.html',
            {'form':formEditar, 'mensaje':'Error - Editar orden'})
        
def borrarOrden(request, id):
    ordenBorrar = Orden.objects.get(pk=id)
    ordenBorrar.delete()
    return redirect('listaOrdenes')

def estadoOrden(request, id):
    ordenEstado = Orden.objects.get(pk=id)
    
    if ordenEstado.estado == False:
        ordenEstado.estado = True
        ordenEstado.save()
    elif ordenEstado.estado == True:
        ordenEstado.estado = False
        ordenEstado.save()
    return redirect('listaOrdenes')
    