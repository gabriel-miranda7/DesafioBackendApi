## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Sobre](#sobre)
- [Model](#model)


## Instalação
Para o seguinte projeto, foi utilizado um ambiente virtual para instalação das dependências. O uso é opcional, você pode pular direto para o 3° comando se não quiser usar o ambiente ou pular esta secção se já tiver instaladas as dependências em sua máquina. Para configurar seu ambiente você deve executar o seguintes comandos:

<br>

`python3 -m venv .env` 

`.env\Scripts\activate`  Caso surja um erro altere as permissões de execução de scripts do seu SO.

`pip install -r requirements.txt`

Pronto! Agora você deve ter seu ambiente virtual configurado e as dependências instaladas.

## Uso
Para iniciar o servidor entre no diretório raiz e pelo prompt e digite

`python manage.py runserver`

Agora você pode fazer requisições HTTP para a API utilizando o Postman, por exemplo. 

## Sobre
Essa Api foi criada com a temática concessionária. Você pode adcionar, editar, receber e deletar dados sobre o model carro que implementei. (CRUD completo). Como requisitado, não foi implementado nenhum front-end, apenas as respostas do servidor em formado JSON.

## Model
O model carro encontrado em `/carsApi/models.py` possui os seguintes atributos:<br>
<ul>
    <li>
        nome : String de até 50 caracteres
    </li>
    <li>
        description : String de até 600 caracteres
    </li>
    <li>
        valor : Inteiro Positivo
    </li>
    <li>
        ano : Inteiro Positivo entre 1900 e 2024
    </li>
    <li>
        cor : String que pode ser escolhida dentre as alternativas: [Azul, Branco, Prata, Preto, Vermelho]
    </li>
</ul>

<h2>Obrigado!</h2>