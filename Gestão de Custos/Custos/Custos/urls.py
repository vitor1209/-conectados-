"""
URL configuration for Custos project.

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
from user.views import signup, signin
from contas.views import home, novaDespesa, DespesasListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin, name='signin'),
    path('signup/',signup, name='signup'),
    path('home/',home, name='home'),
    path('nova-despesa/', novaDespesa, name='novaDespesa'),
    path('despesasLista/', DespesasListView.as_view(), name='despesasLista'),
]
