
from django.shortcuts import redirect, render
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def listar_clientes(request):
  clientes = Cliente.objects.all()
  return render(request, 'clientes/listar_clientes.html', {'clientes' : clientes})

def cadastrar_cliente(request):
  if request.method == 'POST':
    form = ClienteForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('listar_clientes')
  else:
    form = ClienteForm()
  return render(request, 'clientes/form_cliente.html', {'form': form})

def listar_cliente_id(request, id):
  cliente = Cliente.objects.get(id=id)
  return render(request, 'clientes/lista_cliente.html', {'cliente': cliente})

def editar_cliente(request, id):
  cliente = Cliente.objects.get(id=id)
  form = ClienteForm(request.POST or None, instance=cliente)
  if form.is_valid():
    form.save()
    return redirect('listar_clientes')
  return render(request, 'clientes/form_cliente.html', {'form': form})

def remover_cliente(request, id):
  cliente = Cliente.objects.get(id=id)
  if request.method == 'POST':
    cliente.delete()
    return redirect('listar_clientes')
  return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente}) 





