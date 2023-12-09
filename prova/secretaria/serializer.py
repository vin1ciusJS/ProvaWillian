from .models import Secretaria
from rest_framework import serializers
class SecretariaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secretaria
        fields = [
            "nome_funcionario",
            "matricula_funcionario",
            "telefone",
            "funcao",
            "setor",
            "dataNascimento",
            "idade"
        ]