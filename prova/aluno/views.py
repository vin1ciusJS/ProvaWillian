from django.shortcuts import render
from aluno.models import Aluno
from aluno.serializer import AlunoSerializer
from rest_framework import viewsets

# Create your views here.
class AlunoViews(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer