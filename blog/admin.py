from django.contrib import admin
from .models import Categoria
from .models import Computadora
from .models import Marca

admin.site.register(Categoria)
admin.site.register(Computadora)
admin.site.register(Marca)
# Register your models here.
