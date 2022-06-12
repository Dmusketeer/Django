from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import About

def about(request):
    frnds=About.objects.all().values()
    template = loader.get_template('about.html')
    context = {
    'frnds': frnds,
  } 
    return HttpResponse(template.render(context,request))

