from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import About

def about(request):
    frnds=About.objects.all().values()
    output=''
    for x in frnds:
        output+=x["firstname"]
    return HttpResponse(f'<h1>{output[0:7]}<h1/>')


