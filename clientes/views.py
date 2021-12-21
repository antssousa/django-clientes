
from django.shortcuts import redirect, render
from .models import Cliente
from .forms import ClienteForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def listar_clientes(request):
  clientes = Cliente.objects.all()
  return render(request, 'clientes/listar_clientes.html', {'clientes' : clientes})

@login_required()
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

@login_required()
def editar_cliente(request, id):
  cliente = Cliente.objects.get(id=id)
  form = ClienteForm(request.POST or None, instance=cliente)
  if form.is_valid():
    form.save()
    return redirect('listar_clientes')
  return render(request, 'clientes/form_cliente.html', {'form': form})

@login_required()
def remover_cliente(request, id):
  cliente = Cliente.objects.get(id=id)
  if request.method == 'POST':
    cliente.delete()
    return redirect('listar_clientes')
  return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente}) 


def cadastrar_usuario(request):
  if request.method == 'POST':
    form_usuario = UserCreationForm(request.POST)
    if form_usuario.is_valid():
      form_usuario.save()
      return redirect('listar_clientes')
  else:
    form_usuario = UserCreationForm()
  return render(request, 'clientes/form_usuario.html', {'form_usuario': form_usuario})

def logar_usuario(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    usuario = authenticate(request, username=username, password=password)
    if usuario is not None:
      login(request, usuario)
      return redirect('listar_clientes')
    else:
      messages.error(request, 'As credenciais estão incorretas')
      return redirect('logar_usuario')
  else:
    form_login = AuthenticationForm()
  return render(request, 'clientes/form_login.html', {'form_login': form_login})


def deslogar_usuario(request):
  logout(request)
  return redirect('logar_usuario')



