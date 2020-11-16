from django.shortcuts import render

# Create your views here.

def graph(request):
    return render(request,'show.html')

def ceshi(request):
    return render(request,'test.html')