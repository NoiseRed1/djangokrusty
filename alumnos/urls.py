# alumnos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compra/', views.compra, name='compra'),
    path('envivo/', views.envivo, name='envivo'),
    path('info/', views.info, name='info'),
    path('resena/', views.resena, name='resena'),
    path('login/', views.login, name='login'),
    path('login/index.html', views.index, name='volverLogin'),
    path('login/login.html', views.login, name='iniciosesion'),
    
    
]
