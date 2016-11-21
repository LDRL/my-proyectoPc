from django.conf.urls import include, url
from django.contrib import admin
#from django.contrib import settings
urlpatterns = [
    # Examples:
    # url(r'^$', 'misitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
#    url(r'^media/(?P<path>.*)$','django.views.statict.serve',{'document_root':settings_MEDIA_ROOT}),
]
