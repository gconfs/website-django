from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.template import RequestContext, loader

from .models import Board

# Create your views here.

def index(request):
    template = loader.get_template('status/index.html')
    board = Board.objects.get(board_year=timezone.now().year)
    context = RequestContext(request, {'board': board})
    return HttpResponse(template.render(context))
