from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

from .models import Member

# Create your views here.

def index(request):
    template = loader.get_template('team/index.html')
    team = Member.objects.all()
    context = RequestContext(request, {'team': team})
    return HttpResponse(template.render(context))
