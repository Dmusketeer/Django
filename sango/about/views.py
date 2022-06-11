from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("<h1>Hey You Are on About page <h1/>")

    