from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Stream
# Create your views here.

def index(request):
    streams = Stream.objects.all()
    template = loader.get_template('stream/index.html')
    context = RequestContext(request, {'streams': streams})
    return HttpResponse(template.render(context))
