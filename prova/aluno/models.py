from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=80)
    endereco = models.CharField(max_length=80)
    idade = models.IntegerField()
    curso = models.CharField(max_length=80)