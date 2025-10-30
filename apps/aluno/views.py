from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Cadastro(request):
    return render(request, 'aluno/cadastro.html')