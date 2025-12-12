from apps.aluno.models import Aluno
from django import forms

class AlunoForms(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ["",]
        labels = {
            "matricula": "Matricula",
            "status": "Ativo"
        }
        widgets = {
            "nome":forms.TextInput(attrs={"class": "form-control", "autoFocus": "autofocus"}),
            "matricula":forms.TextInput(attrs={"class": "form-control"}),
            "email":forms.EmailInput(attrs={"class": "form-control"}),
            "telefone":forms.TextInput(attrs={"class": "form-control"}),
            "status":forms.CheckboxInput(attrs={"class": "form-control form-check-list"}),
        }