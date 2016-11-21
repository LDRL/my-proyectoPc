from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.index),
        url(r'^categoria/$', views.listado),
        url(r'^categoria/nuevo/$', views.Ccreate,),
    ]
