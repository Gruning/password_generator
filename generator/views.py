from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'generator/home.html',{'password': '123456'})

def food(request):
    return HttpResponse('<h1>food is ready</h1>')
# Create your views here.
