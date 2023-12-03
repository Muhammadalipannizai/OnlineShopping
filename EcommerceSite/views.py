from django.shortcuts import render
from django.http import HttpResponse

def temp(request):
    return render(request,'home.html')