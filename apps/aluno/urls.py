from django.urls import path
from apps.aluno.views import index, cadastro

urlpatterns = [
    path("", index, name="index"),
    path("cadastro/", cadastro, name="cadastro")
]