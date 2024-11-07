
from django.urls import path, include

from . import views

urlpatterns=[

    path('base/', views.base,name='base'),
    path('info/',views.info,name='info'),
    path('info1/',views.info1,name='info1'),
    path('login/',views.login,name='login'),
    path('validar_login', views.validar_login, name='validar_login'),
]