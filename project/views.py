from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.template import loader


def index(request):
    template = loader.get_template('project/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def photographs(request):
    photographs = Photographs.objects.all()
    template = loader.get_template('project/photographs.html')
    context = {'photographs': photographs}
    return HttpResponse(template.render(context, request))

def info(request, photograph_id):
    info = get_object_or_404(Photographs, id=photograph_id)
    template = loader.get_template('project/info.html')
    context = {'info': info}
    return HttpResponse(template.render(context, request))