from django.shortcuts import render
from .models import Categoria

def index(request):
    return render(request, 'blog/index.html', {})

def listado(request):
    return render(request, 'blog/categoria/listado.html',{})

#def index(request):
#    return render(request, 'blog/index.html'.{})
# Create your views here.
