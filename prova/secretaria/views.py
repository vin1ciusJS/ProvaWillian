from django.shortcuts import render
from secretaria.models import Secretaria
from secretaria.serializer import SecretariaSerializer
from rest_framework import viewsets

# Create your views here.
class SecretariaViews(viewsets.ModelViewSet):
    queryset = Secretaria.objects.all()
    serializer_class = SecretariaSerializer