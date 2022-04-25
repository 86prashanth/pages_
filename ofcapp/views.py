
from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
    return HttpResponse('<center>This is first html</center>')

def first(request):
    return render(request,'first.html')