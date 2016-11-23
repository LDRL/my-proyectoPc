from django.conf.urls import include, url
from . import views
from django.conf import settings
urlpatterns = [
        url(r'^$',views.ingresar),
        url(r'^registro/$',views.RegistroUsuario),

        url(r'^privado/$',views.privado),
        url(r'^cerrar/$', views.cerrar),
        url(r'^home/$', views.index),
        url(r'^categoria/$', views.listado),
        url(r'^categoria/nuevo/$', views.Ccreate,),
        url(r'^categoria/(?P<pk>[0-9]+)/edit/$', views.Cedit,),
        url(r'^categoria/(?P<pk>[0-9]+)/delete/$', views.Cdelete,),
        url(r'^marca/$', views.Mlistado,),
        url(r'^marca/nuevo/$', views.Mcreate,),
        url(r'^marca/(?P<pk>[0-9]+)/edit/$', views.Medit,),
        url(r'^marca/(?P<pk>[0-9]+)/delete/$', views.Mdelete,),
        url(r'^computadora/$', views.Compulistado,),
        url(r'^computadora/nuevo/$',views.Compucreate,),
        url(r'^computadora/(?P<pk>[0-9]+)/edit/$', views.Compuedit,),
        url(r'^computadora/(?P<pk>[0-9]+)/delete/$', views.Compudelete,),



    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),

#        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#        'document_root': settings.MEDIA_ROOT}),
#        (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),

#        url(r'^computadora/$', views.Compulistado,),
    ]
