from django.db import models

COLOR_CHOICES = [   # Lista de tuplas com pares de valores com as cores possíveis
    ('Azul', 'Azul'),
    ('Branco', 'Branco'),
    ('Prata', 'Prata'),
    ('Preto', 'Preto'),
    ('Vermelho', 'Vermelho'),
]


class Car(models.Model): #Define a classe Car, que possui os atributos de um carro 
    nome = models.CharField(max_length=50, default='', blank=True)
    description = models.CharField(max_length=600, blank=True)
    valor = models.PositiveIntegerField() #Assumindo que o valor dos carros não possuem centavos.
    ano = models.PositiveIntegerField() 
    cor = models.CharField(choices = COLOR_CHOICES, default='Preto', max_length=10) #Permite a api receber uma das cores na lista color_choices.

    def __str__(self):  #Formata o nome do carro no painel admin
        return self.nome + ", " + self.description[0:20] + '...'
