from django.http import JsonResponse
from .models import Car
from  .serializers import carSerializer
from rest_framework.decorators import api_view #Importa o decorator @api_view
from rest_framework.response import Response #Importa o response
from rest_framework import status #Importa os status http




#Endpoint do serializer CarList

@api_view(['GET', 'POST', 'DELETE'])
def car_List(request):

    if (request.method == 'GET'): #MÉTODO GET
        todos_carros = Car.objects.all() #atribui todos os objetos python car á variável
        serializer = carSerializer(todos_carros, many=True) #Serializa os objetos
        return JsonResponse({'carros' : serializer.data}) #Retorna a resposta em Json
    
    elif (request.method == 'POST'): #MÉTODO POST
        serializer = carSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #Retorna o status 201
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == 'DELETE'):
        confirmacao = request.data.get("confirm", False)
        if not confirmacao:
            return Response({"mensagem": "Não foi possível apagar. Para confirmar a exclusão de TODOS os carros adcione o parametro 'confirm' como True."})
        todos_carros = Car.objects.all()
        todos_carros.delete()   #Deleta todos os carros e retorna o status 204 do protocolo HTTP
        return Response({"mensagem": "Sucesso! Todos os carros foram deletados."},status=status.HTTP_200_OK)
    

@api_view(['GET', 'PUT', 'DELETE'])  #Cria um novo endpoind para visualizar o carro por id
def car_Detail(request, id):
    try:
        carro = Car.objects.get(pk = id)   #Receber a primary key como id
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) #Caso o carro não exsta na lista, retorna o erro
    
    if (request.method == 'GET'): #Cria o método get
        serializer = carSerializer(carro)
        return JsonResponse({'carro' : serializer.data})
     
    elif (request.method == 'PUT'): #Cria o método put
        serializer = carSerializer(carro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({'carro' : serializer.data})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif (request.method == 'DELETE'):
        carro.delete()   #Deleta e retorna o status 204 do protocolo HTTP
        return Response(status=status.HTTP_204_NO_CONTENT)