from django.db.models import Sum
from django.shortcuts import render
from .models import Usuario,Registro,Material,Beneficio
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


def info2(request):
    print("estoy en info1")
    context={}
    return render(request,"aplicacion/info2.html",context)


def login(request):
    context = {}
    return render(request, "aplicacion/login.html", context)


def validar_login(request):
    print("Estoy en validar login")
    context = {}
    
    if request.method == "POST":
        print("Ingreso al POST")

        rut = request.POST["rut"]
        contraseña = request.POST["contraseña"]

        try:
            # Buscar al usuario por su RUT
            usuario = Usuario.objects.get(rut=rut)
            # Validar la contraseña (esto es solo un ejemplo; considera usar contraseñas encriptadas)
            if usuario.contraseña == contraseña:
                # Configurar la sesión
                request.session["user"] = f"{usuario.nombre} {usuario.apellido}"
                request.session["user_role"] = usuario.rol
                request.session["user_puntos"] = usuario.puntos
                request.session["user_rut"]=usuario.rut
                return redirect('base')
            else:
                context['mensaje'] = 'Contraseña incorrecta'
        except Usuario.DoesNotExist:
            context['mensaje'] = 'Usuario no encontrado'
    
    return render(request, 'aplicacion/login.html', context)


def registro(request):
    print("Estoy en registro")
    context = {}
    return render(request, "aplicacion/registro.html", context)


def validar_registro(request):
    print("Estoy en validar_registro")
    context={}
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        contraseña = request.POST["contraseña"]
        telefono=request.POST["telefono"]
        direccion=request.POST["direccion"]
        correo=request.POST["correo"]
        rol=request.POST["rol"]

        nuevo_usuario = Usuario(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            contraseña=contraseña, 
            telefono=telefono,
            direccion=direccion,
            correo=correo,
            rol=rol
        )
        nuevo_usuario.save()
        context["mensaje"] = "Usuario registrado con éxito"
        return render(request, "aplicacion/registro.html", context)
    
    return render(request, "aplicacion/registro.html", context)


def panel_control(request):
    print("esttoy en panel_control")
    context={}
    return render(request,"aplicacion/panel_control.html",context)        


def cerrar_sesion(request):
    # Elimina los datos de la sesión relacionados con el usuario
    request.session.flush()  # Esto elimina todos los datos de la sesión
    
    return redirect('base')


def registro_material(request):
    print("estoy en registro material")
    context={}
    return render(request,"aplicacion/registro_material.html",context)


def validar_registro_material(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        material_nombre = request.POST["nombre"]
        peso = float(request.POST["peso"])  # Asegúrate de convertir el peso a float si es necesario
        
        try:
            # Buscar usuario por RUT
            usuario = Usuario.objects.get(rut=rut)
            
            # Buscar material por nombre
            material = Material.objects.get(nombre=material_nombre)
            
            # Calcular puntos ganados
            puntos_ganados = peso * material.valor  # Se usa el valor del material directamente
            
            # Crear y guardar el nuevo registro
            nuevo_registro = Registro(
                usuario=usuario,
                material=material,
                peso=peso
            )
            nuevo_registro.save()
            
            # Actualizar puntos del usuario
            usuario.puntos += puntos_ganados
            usuario.save()  
            
            return redirect('panel_control') 

        except Usuario.DoesNotExist:
            return render(request, 'aplicacion/registro_material.html', {'error': 'Usuario no encontrado'})
        except Material.DoesNotExist:
            return render(request, 'aplicacion/registro_material.html', {'error': 'Material no encontrado'})
    else:
        return render(request, 'aplicacion/registro_material.html')


def beneficios(request):
   
    beneficios= Beneficio.objects.all()
    context ={'beneficios': beneficios }


    return render(request, 'aplicacion/beneficios.html', context)


def registro_beneficio(request):
    print("Estoy en registro beneficio")
    context={}
    return render(request, 'aplicacion/registro_beneficio.html', context)


def validar_beneficio(request):
    print("Estoy en validar beneficio")
    context={}
    if request.method == "POST":
        titulo = request.POST["titulo"]
        fecha_inicio = request.POST["fecha_inicio"]
        fecha_fin = request.POST["fecha_fin"]
        costo = request.POST["costo"]
        empresa = request.POST["empresa"]

        nuevo_beneficio= Beneficio(
            titulo=titulo,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            costo=costo,
            empresa=empresa
        )
        nuevo_beneficio.save()
        context["mensaje"]="Beneficio guardado con éxito"
        return render(request,"aplicacion/registro_beneficio.html",context)
    else:
        context["mensaje"]="Error, beneficio no guardado"
        return render(request,"aplicacion/registro_beneficio.html",context)
    
    
def canjear_beneficio(request, beneficio_id):
    print("Estoy en canjear_beneficio")
    context = {}
    
    try:
        beneficio = Beneficio.objects.get(pk=beneficio_id) 
        context = {
            'titulo': beneficio.titulo,
            'costo': beneficio.costo,
            'beneficio_id':beneficio.id
        }
    except Beneficio.DoesNotExist:
        context['error'] = "El beneficio no existe"

    return render(request, "aplicacion/canjear_beneficio.html", context)


def confirmar_canje(request, beneficio_id):
    if request.method == "POST":
        usuario_rut=request.POST["rut"]

        try:
            beneficio = Beneficio.objects.get(pk=beneficio_id)
            usuario = Usuario.objects.get(rut=usuario_rut)

            if usuario.puntos >= beneficio.costo:
                usuario.puntos -= beneficio.costo
                usuario.save()

                return render(request, "aplicacion/canje_exitoso.html", {'beneficio': beneficio})
            else:
                return render(request, "aplicacion/canjear_beneficio.html", {
                    'error': 'No tienes suficientes puntos para canjear este beneficio.',
                    'titulo': beneficio.titulo,
                    'costo': beneficio.costo
                })

        except Beneficio.DoesNotExist:
            return render(request, "aplicacion/canjear_beneficio.html", {'error': 'El beneficio no existe'})
        except Usuario.DoesNotExist:
            return render(request, "aplicacion/canjear_beneficio.html", {'error': 'Usuario no encontrado'})

    return redirect('beneficios')


def canje_exitoso(request):
    print("canje exitoso")
    context={}
    return render(request, "aplicacion/canje_exitoso.html",context)


def historial_reciclaje(request):
    registros = Registro.objects.filter(usuario=request.user)
    
    total_reciclado = registros.aggregate(total=Sum('peso'))['total'] or 0  

    return render(request, 'aplicacion/historial_reciclaje.html', {
        'registros': registros,
        'total_reciclado': total_reciclado
    })


def historial_admin(request):
    if request.session.get("user_role") != "admin":
        return redirect('base')  
    registros = Registro.objects.all()
    return render(request, 'aplicacion/historial_admin.html', {'registros': registros})

