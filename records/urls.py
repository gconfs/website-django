from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='records_index'),
        url(r'^(?P<record_id>[0-9]+)$', views.details, name='records_details'),
        ]
