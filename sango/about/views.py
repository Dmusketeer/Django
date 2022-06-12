from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import About

def about(request):
    frnds=About.objects.all().values()
    template = loader.get_template('about.html')
    context = {
    'frnds': frnds,
  } 
    return HttpResponse(template.render(context,request))

def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    about=About(firstname=x,lastname=y).save()
    return HttpResponseRedirect(reverse('about'))

