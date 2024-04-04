from rest_framework import serializers
from .models import Car

class carSerializer(serializers.ModelSerializer): #Classe que define um serializer
    class Meta:
        model = Car
        fields = ['id', 'nome', 'description', 'valor', 'ano', 'cor']
    
    def validate_ano(self, valor): #Limita o ano do carro, gerando bad request em caso de erro
        if valor < 1900 or valor > 2024:
            raise serializers.ValidationError("O ano do carro deve estar entre 1900 e 2024.")
        return valor
