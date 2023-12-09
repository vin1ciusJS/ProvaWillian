from django.db import models

# Create your models here.
class Secretaria(models.Model):
    nome_funcionario = models.CharField(max_length=80)
    matricula_funcionario = models.IntegerField()
    telefone = models.CharField(max_length=80)
    funcao = models.CharField(max_length=80)
    setor = models.CharField(max_length=80)
    dataNascimento = models.DateField()
    idade = models.IntegerField()