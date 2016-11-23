from django.shortcuts import render
from .models import Categoria, Marca, Computadora
from .forms import CategoriaForm, MarcaForm
from .forms import CompuForm
from django.shortcuts import redirect,get_object_or_404
from django.contrib import messages
import json
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def logueo(request):
    return render(request, 'blog/login.html',{})

@login_required(login_url='ingresar')
def index(request):
    usuario = request.user
    return render(request,'blog/index.html',{'usuario':usuario})

@login_required(login_url='ingresar')
def listado(request):
    categorias = Categoria.objects.filter()
    return render(request, 'blog/categoria/listado.html',{'categorias':categorias})

@login_required(login_url='ingresar')
def Ccreate(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cate = form.save(commit=False)
            cate.save()
        messages.add_message(request, messages.SUCCESS, 'categoria Guardada Exitosamente')
        return redirect('blog.views.listado')
    else:
        form = CategoriaForm()
    return render(request, 'blog/categoria/create.html',{'form': form})

@login_required(login_url='ingresar')
def Cedit(request, pk):
     categoria = get_object_or_404(Categoria, pk=pk)
     if request.method == "POST":
         form = CategoriaForm(request.POST, instance=categoria)
         if form.is_valid():
             categoria = form.save(commit=False)
             categoria.save()
             return redirect('blog.views.listado')
     else:
         form = CategoriaForm(instance=categoria)
         return render(request, 'blog/categoria/edit.html', {'form': form})

@login_required(login_url='ingresar')
def Cdelete(request, pk):
     categoria = Categoria.objects.get(pk=pk)
     if request.method == "POST":
         categoria.delete()
         return redirect('blog.views.listado')
     return render(request, 'blog/categoria/delete.html', {'categoria': categoria})

@login_required(login_url='ingresar')
def Mlistado(request):
    marcas = Marca.objects.filter()
    return render(request, 'blog/marca/index.html',{'marcas':marcas})

@login_required(login_url='ingresar')
def Mcreate(request):
    if request.method == "POST":
        formulario = MarcaForm(request.POST)
        if formulario.is_valid():
            marc = formulario.save(commit=False)
            marc.save()
        messages.add_message(request, messages.SUCCESS, 'Marca Guardada Exitosamente')
        return redirect('blog.views.Mlistado')
    else:
        formulario = MarcaForm()
    return render(request, 'blog/marca/create.html',{'form': formulario})

@login_required(login_url='ingresar')
def Medit(request, pk):
     marca = get_object_or_404(Marca, pk=pk)
     if request.method == "POST":
         form = MarcaForm(request.POST, instance=marca)
         if form.is_valid():
             marca = form.save(commit=False)
             marca.save()
             return redirect('blog.views.Mlistado')
     else:
         form = MarcaForm(instance=marca)
         return render(request, 'blog/marca/create.html', {'form': form})

@login_required(login_url='ingresar')
def Mdelete(request, pk):
     marca = Marca.objects.get(pk=pk)
     if request.method == "POST":
         marca.delete()
         return redirect('blog.views.Mlistado')
     return render(request, 'blog/marca/delete.html', {'marca': marca})

@login_required(login_url='ingresar')
def Compulistado(request):
    computadoras = Computadora.objects.filter()
    return render(request, 'blog/computadora/index.html',{'computadoras':computadoras})

@login_required(login_url='ingresar')
def Compucreate(request):
    if request.method == "POST":
        formulario = CompuForm(request.POST,request.FILES)
        if formulario.is_valid():
            marc = formulario.save(commit=False)
            marc.save()
        messages.add_message(request, messages.SUCCESS, 'Computadora Guardada Exitosamente')
        return redirect('blog.views.Compulistado')
    else:
        formulario = CompuForm()
    return render(request, 'blog/computadora/create.html',{'form': formulario})

@login_required(login_url='ingresar')
def Compuedit(request, pk):
     computadora = get_object_or_404(Computadora, pk=pk)
     if request.method == "POST":
         form = CompuForm(request.POST, instance=computadora)
         if form.is_valid():
             computadora = form.save(commit=False)
             computadora.save()
             return redirect('blog.views.Compulistado')
     else:
         form = CompuForm(instance=computadora)
         return render(request, 'blog/computadora/create.html', {'form': form})

@login_required(login_url='ingresar')
def Compudelete(request, pk):
     computadora = Computadora.objects.get(pk=pk)
     if request.method == "POST":
         computadora.delete()
         return redirect('blog.views.Compulistado')
     return render(request, 'blog/computadora/delete.html', {'computadora': computadora})

###login
##
#

@login_required(login_url='ingresar')
def RegistroUsuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog.views.index')
    else:
        form = UserCreationForm()
    return render(request, 'blog/usuario/registrar.html', {'form': form})

def ingresar(request):
    if not request.user.is_anonymous():
        return redirect('/privado')
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            usuario = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=usuario, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('blog.views.index')
                else:
                    return render(request,'blog/usuario/noactivo.html',{})
            else:
                return render(request,'blog/usuario/nousuario.html',{})
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

@login_required(login_url='ingresar')
def privado(request):
    usuario = request.user
    return render(request,'blog/usuario/privado.html',{'usuario':usuario})

@login_required(login_url='ingresar')
def cerrar(request):
    logout(request)
    return redirect('blog.views.ingresar')
