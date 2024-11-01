"""
URL configuration for SistemaEnquete project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios.views import user, listagem, forms , updateEnquete , deleteEnquete, opcoesEnquete, resultado


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user),
    path('enquete/', listagem , name='Enquete'),
    path('newEnquete/', forms, name='newEnquete'),
    path('enquete_update/<int:pk>/', updateEnquete, name='enqueteUpdate'),
    path('enquete_delete/<int:pk>/', deleteEnquete, name='enquetedelete'),
    path('enquete_opcoes/<int:pk>/', opcoesEnquete, name='enqueteopcoes'),
    path('resultado/<int:pk>/', resultado, name='resultado'),
]