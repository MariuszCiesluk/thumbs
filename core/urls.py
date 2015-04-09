from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'galeria/(?P<size>\w+)/$', views.thumbnail,
        name='thumbnail'),
                     
)

