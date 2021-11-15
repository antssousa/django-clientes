from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = ['nome', 'email', 'profissao', 'sexo', 'data_nascimento']