from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return HttpResponse("this is contact page")