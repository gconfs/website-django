from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='confs_index'),
        url(r'^(?P<conf_id>[0-9]+)$', views.details, name='confs_details'),
        ]
