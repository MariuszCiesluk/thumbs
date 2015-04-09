from django.conf.urls import patterns, include, url
from thumbs.core import views


urlpatterns = patterns('',
    url(r'galeria/(?P<size>\w+)/$', view.thumbnail,
        name='thumbnail'),
                     
)

