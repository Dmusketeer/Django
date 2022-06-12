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

def delete(request,id):
    about= About.objects.get(id=id)
    about.delete()
    return HttpResponseRedirect(reverse('about'))

def update(request,id):
    about=About.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        "about":about,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    first=request.POST['first']
    last=request.POST['last']
    about= About.objects.get(id=id)
    about.firstname=first
    about.lastname=last
    about.save()
    return HttpResponseRedirect(reverse('about'))

    



