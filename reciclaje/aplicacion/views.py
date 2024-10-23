from django.shortcuts import render

# Create your views here.

def base(request):
    print("Hola, estoy en base")
    context={}
    return render(request,'aplicacion/base.html',context)

def info(request):
    print("estoy en info")
    context={}
    return render(request,"aplicacion/info.html",context)

def info1(request):
    print("estoy en info1")
    context={}
    return render(request,"aplicacion/info1.html",context)