
from django.urls import path, include

from . import views

urlpatterns=[

    path('base/', views.base,name='base'),
    path('info/',views.info,name='info'),
    path('info1/',views.info1,name='info1'),
    path('login/',views.login,name='login'),
    path('beneficios/',views.beneficios,name='beneficios'),
    path('validar_login', views.validar_login, name='validar_login'),
    path('registro',views.registro,name='registro'),
    path('validar_registro',views.validar_registro,name='validar_registro'),
    path('panel_control', views.panel_control,name='panel_control'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('registro_material/', views.registro_material, name='registro_material'),
    path('validar_registro_material/', views.validar_registro_material, name='validar_registro_material'),
    path('registro_beneficio/', views.registro_beneficio, name='registro_beneficio'),
    path('validar_beneficio/', views.validar_beneficio, name='validar_beneficio'),
     path('canjear_beneficio/<int:beneficio_id>/', views.canjear_beneficio, name='canjear_beneficio'),
     path('confirmar_canje/<int:beneficio_id>/', views.confirmar_canje, name='confirmar_canje'),
      path('canje_exitoso', views.validar_beneficio, name='validar_beneficio'),

]