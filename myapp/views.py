from django.shortcuts import render
from django.http import HttpResponse
from math import factorial
# Create your views here.

def index(request):
    return HttpResponse("<h1>welcome to views of an app</h1>")

def home(request):
    return render(request,"myapp/home.html",{'name':"pradeep"})

def child(request):
    return render(request,"child.html")

def sam(request):
    return render(request,"myapp/sam.html")