from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Conf

# Create your views here.

def index(request):
    template = loader.get_template('confs/index.html')
    conf_list = Conf.objects.all()
    context = RequestContext(request, {'conf_list': conf_list})
    return HttpResponse(template.render(context))

def details(request, conf_id):
    template = loader.get_template('confs/details.html')
    conf = get_object_or_404(Conf, pk=conf_id)
    context = RequestContext(request, {'conf': conf})
    return HttpResponse(template.render(context))
