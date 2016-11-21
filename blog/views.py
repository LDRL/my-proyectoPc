from django.shortcuts import render
from .models import Categoria
from .forms import CategoriaForm
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


#def index(request):
#    return render(request, 'blog/index.html'.{})
# Create your views here.
