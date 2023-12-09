"""
URL configuration for prova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, viewsets
from aluno.views import AlunoViews
from aluno.serializer import AlunoSerializer
from aluno.models import Aluno
from secretaria.views import SecretariaViews
from secretaria.serializer import SecretariaSerializer
from secretaria.models import Secretaria


rotas = routers.DefaultRouter()
rotas.register("Aluno", AlunoViews),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rotas.urls))
]

class AlunoViews(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class SecretariaViews(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = SecretariaSerializer