from django.urls import path, include
from .views import visualizacao
from usuarios.views import listagem

urlpatterns = [
    path("", listagem, name="Enquete"),
    path("signup/", visualizacao, name="visualizacao"),
    path("accounts/", include("django.contrib.auth.urls")),
]