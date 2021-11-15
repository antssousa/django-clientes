from django.db import models

# Create your models here.
class Cliente(models.Model):
  SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outros')
  )
  nome = models.CharField('Nome', max_length=100, null=False, blank=False)
  email = models.EmailField('E-mail', null=False, blank=False)
  profissao = models.CharField('Profissão', max_length=50, null=False, blank=False)
  sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
  data_nascimento = models.DateField('Data de nascimento', null=False, blank=False)

  def __str__(self):
    return self.nome
