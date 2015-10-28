"""gconfs_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin$', RedirectView.as_view(url='/admin/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^confs$', RedirectView.as_view(url='/confs/')),
    url(r'^confs/', include('confs.urls')),
    url(r'^team$', RedirectView.as_view(url='/team/')),
    url(r'^team/', include('team.urls')),
    url(r'^statuts$', RedirectView.as_view(url='/statuts/')),
    url(r'^statuts/', include('statuts.urls')),
    url(r'^contact$', RedirectView.as_view(url='/contact/')),
    url(r'^contact/', include('contact.urls')),
    url(r'^stream$', RedirectView.as_view(url='/stream/')),
    url(r'^stream/', include('stream.urls')),
    url(r'^[/]?$', include('homepage.urls')),
    url(r'^[0-9a-zA-Z]+[/]?$', include('homepage.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
