from django.conf.urls import url
from . import  views

urlpatterns = [
    # /videos/
    url(r'^index/$', views.index, name='index'),

    # /videos/list
    url(r'^$', views.list, name='list'),

    # /videos/videoId
    url(r'^((?P<videoId>[0-9]+)/(?P<name>[0-9a-zA-Z]+))/$', views.detail, name='detail')
]
