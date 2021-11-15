
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



