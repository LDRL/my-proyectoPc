from django.shortcuts import render
from .models import Categoria, Marca, Computadora
from .forms import CategoriaForm, MarcaForm
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    return render(request, 'blog/index.html', {})

def listado(request):
    categorias = Categoria.objects.filter()
    return render(request, 'blog/categoria/listado.html',{'categorias':categorias})

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

def Mlistado(request):
    marcas = Marca.objects.filter()
    return render(request, 'blog/marca/index.html',{'marcas':marcas})

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

def Compulistado(request):
    computadoras = Computadora.objects.filter()
    return render(request, 'blog/computadora/index.html',{'computadoras':computadoras})


#def index(request):
#    return render(request, 'blog/index.html'.{})
# Create your views here.
