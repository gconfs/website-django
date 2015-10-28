from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^thanks/$', views.thanks, name='thanks'),
        url(r'^thanks$', views.thanks, name='thanks'),
        url(r'^robots/$', views.robots, name='robots'),
        url(r'^robots$', views.robots, name='robots'),
        url(r'^error/$', views.error, name='error'),
        url(r'^error$', views.error, name='error'),
        ]
