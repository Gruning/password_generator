from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'generator/home.html',{'password': '123456'})

def password(request):
    return render(request,'generator/password.html')
# Create your views here.
