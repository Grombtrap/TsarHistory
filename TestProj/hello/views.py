from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'hello/index.html')

def about(request):
    return render(request,'hello/about.html')

def contact(request):
    return render(request,'hello/contact.html')