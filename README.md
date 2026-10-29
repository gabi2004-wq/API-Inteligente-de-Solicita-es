# API-Inteligente-de-Solicita-es
A API Inteligente de Solicitações é uma aplicação desenvolvida em Python para gerenciar solicitações de uma empresa. O projeto permite listar, criar, consultar e excluir solicitações por meio de endpoints REST.  A documentação interativa é disponibilizada pelo Swagger UI, facilitando os testes e a utilização da API.
Tecnologias utilizadas

Python

FastAPI

Swagger UI

REST API

Git e GitHub

Funcionalidades

Consultar a página inicial da API.

Listar todas as solicitações.

Criar novas solicitações.

Consultar uma solicitação específica por ID.

Excluir uma solicitação por ID.

Testar os endpoints pela documentação interativa.

Endpoints disponíveis

Método

Endpoint

Descrição

GET

/

Página inicial da API

GET

/solicitacoes

Lista as solicitações

POST

/solicitacoes

Cria uma solicitação

GET

/solicitacoes/{solicitacao_id}

Consulta uma solicitação por ID

DELETE

/solicitacoes/{solicitacao_id}

Exclui uma solicitação por ID

Como executar o projeto

1. Clone o repositório

git clone URL_DO_SEU_REPOSITORIO

Substitua URL_DO_SEU_REPOSITORIO pelo endereço HTTPS do seu repositório no GitHub.

2. Entre na pasta do projeto

cd nome-da-pasta-do-projeto

3. Crie um ambiente virtual

python -m venv venv

4. Ative o ambiente virtual no Windows

venv\Scripts\activate

5. Instale as dependências

pip install -r requirements.txt

6. Execute a aplicação

Se o arquivo principal se chamar main.py e a aplicação FastAPI estiver definida como app, execute:

uvicorn main:app --reload

Se o arquivo principal tiver outro nome, ajuste o comando conforme a estrutura do projeto.

Documentação da API

Após iniciar a aplicação, acesse:

Swagger UI: http://127.0.0.1:8000/docs

OpenAPI JSON: http://127.0.0.1:8000/openapi.json

Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar o desenvolvimento de APIs com Python, a criação de endpoints REST, a documentação interativa e o gerenciamento de código com Git e GitHub.

Autora

Projeto desenvolvido como parte do meu portfólio de estudos em programação e desenvolvimento de APIs.

