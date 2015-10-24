from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.template import RequestContext, loader

from .models import Board

# Create your views here.

def index(request):
    template = loader.get_template('statuts/index.html')
    print(timezone.now().month)
    try:
        board = Board.objects.get(board_year=timezone.now().year)
    except:
        board = None
    context = RequestContext(request, {'board': board})
    return HttpResponse(template.render(context))
