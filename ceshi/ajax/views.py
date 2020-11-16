from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"ajax.html")

def ajax_add(request):
    num1 = request.POST.get("i1")
    op = request.POST.get("i2")
    num2 = request.POST.get("i3")
    if op == '+':
        ret = int(num1) + int(num2)
    elif op == '-':
        ret = int(num1) - int(num2)
    elif op == '*':
        ret = int(num1) * int(num2)
    elif op == '/':
        ret = int(num1)//int(num2)
    return HttpResponse(ret)