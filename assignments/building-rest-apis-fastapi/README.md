# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar um catálogo de livros usando FastAPI. Você vai praticar rotas HTTP, validação de dados, códigos de status e operações CRUD em uma coleção mantida em memória.

## 📝 Tasks

### 🛠️ Consultar e Buscar Livros

#### Descrição
Complete os endpoints de leitura para listar os livros cadastrados e buscar um livro pelo seu ID. Use a documentação interativa do FastAPI para testar as rotas.

#### Requisitos
O programa concluído deve:

- Iniciar uma aplicação FastAPI chamada `app` no arquivo `starter-code.py`.
- Retornar a lista atual de livros em `GET /books`.
- Retornar um único livro em `GET /books/{book_id}`.
- Responder com status `404` quando o ID solicitado não existir.
- Manter os livros no formato definido pelo modelo `Book`.

### 🛠️ Criar Livros com Validação

#### Descrição
Implemente a criação de livros. A API deve validar o corpo da requisição usando o modelo de entrada do Pydantic e atribuir um ID único ao novo livro.

#### Requisitos
O programa concluído deve:

- Criar um livro por meio de `POST /books` com `title`, `author` e `year`.
- Validar os campos usando o modelo `BookInput`.
- Atribuir um ID ao livro sem substituir os registros existentes.
- Retornar o livro criado com status `201`.
- Deixar o FastAPI rejeitar dados ausentes ou com tipos inválidos.

Exemplo de corpo da requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "year": 1937
}
```

### 🛠️ Atualizar e Remover Livros

#### Descrição
Complete as operações restantes para substituir os dados de um livro existente e removê-lo do catálogo.

#### Requisitos
O programa concluído deve:

- Atualizar todos os campos de um livro por meio de `PUT /books/{book_id}`.
- Retornar o livro atualizado e status `404` se o ID não existir.
- Remover um livro por meio de `DELETE /books/{book_id}`.
- Responder à exclusão com status `204` e sem corpo, ou com status `404` se o ID não existir.
- Permitir verificar as alterações consultando `GET /books`.

## 🚀 Executar e Testar

Instale as dependências e inicie o servidor na pasta da assignment:

```bash
python -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Abra `http://127.0.0.1:8000/docs` para testar os endpoints pela interface interativa. Os dados ficam somente na memória e voltam ao estado inicial quando o servidor reinicia.