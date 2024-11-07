from django.shortcuts import render

from .models import Usuario
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

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

def login(request):
    context = {}
    return render(request, "aplicacion/login.html", context)

def validar_login(request):
    print("Estoy en validar login")
    context={}
    
    if request.method == "POST":
        print("Ingreso al POST")

        rut=request.POST["rut"]
        contraseña=request.POST["contraseña"]


        usuarios=Usuario.objects.all()

        for x in usuarios:
            if x.rut == rut and x.contraseña == contraseña:
                request.session["user"] = f"{x.nombre} {x.apellido}"
                user=request.session["user"]
                context={'usuario':user}
                return render(request,'aplicacion/base.html',context)