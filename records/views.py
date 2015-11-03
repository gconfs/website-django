from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Record

# Create your views here.

def index(request):
    template = loader.get_template('records/index.html')
    record_list = Record.objects.all()
    meeting_records = record_list.exclude(record_is_meeting__exact=False)
    ag_records = record_list.exclude(record_is_meeting__exact=True)
    context = RequestContext(request, {'meeting_records' : meeting_records,
        'ag_records' : ag_records})
    return HttpResponse(template.render(context))

def details(request, record_id):
    template = loader.get_template('records/details.html')
    record = get_object_or_404(Record, pk=record_id)
    context = RequestContext(request, {'record' : record})
    return HttpResponse(template.render(context))
