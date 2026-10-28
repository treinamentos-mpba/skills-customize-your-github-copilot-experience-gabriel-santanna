# 📘 Assignment: Testing FastAPI with pytest

## 🎯 Objective

Escreva testes automatizados para a API de livros criada na assignment Building REST APIs with FastAPI. Use `pytest` e `TestClient` para verificar respostas HTTP, validação de requisições e casos de erro sem iniciar um servidor.

## 📝 Tasks

### 🛠️ Preparar o Cliente de Testes

#### Descrição
Use a implementação concluída da API de livros da assignment anterior. Copie o módulo da aplicação para `main.py` e crie `test_api.py` para os testes.

#### Requisitos
O projeto concluído deve:

- Instalar `pytest`, `fastapi` e `httpx` no ambiente Python.
- Importar `app` de `main.py` e criar um cliente com `TestClient`.
- Executar a suíte com `pytest -q` sem iniciar o servidor Uvicorn.
- Incluir ao menos um teste que confirme que `GET /books` retorna status `200` e uma lista JSON.

Exemplo de configuração do cliente:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
```

### 🛠️ Testar Respostas de Sucesso

#### Descrição
Adicione testes para consultar livros e criar um novo registro. Verifique tanto o status HTTP quanto os dados devolvidos pela API.

#### Requisitos
O projeto concluído deve:

- Confirmar que `GET /books` retorna status `200` e os campos esperados nos livros.
- Confirmar que `GET /books/1` retorna status `200` e os dados do livro de ID `1`.
- Confirmar que `POST /books` com `title`, `author` e `year` válidos retorna status `201`.
- Verificar se a resposta da criação contém os dados enviados e um ID atribuído pela API.
- Manter cada teste independente, sem depender de outro teste ter sido executado antes.

### 🛠️ Verificar Validação e Casos de Erro

#### Descrição
Teste como a API responde a dados inválidos e a IDs que não existem. Garanta também que alterações feitas durante um teste não afetem os demais.

#### Requisitos
O projeto concluído deve:

- Confirmar que uma requisição `POST /books` sem campos obrigatórios retorna status `422`.
- Confirmar que `GET /books/9999`, `PUT /books/9999` e `DELETE /books/9999` retornam status `404`.
- Usar uma fixture do `pytest` para restaurar a coleção e o próximo ID após cada teste que modifica dados.
- Executar toda a suíte com `pytest -q` em mais de uma execução, sem falhas causadas por estado residual.

## 🚀 Executar os Testes

Na pasta do projeto, instale as dependências e execute:

```bash
python -m pip install fastapi httpx pytest
pytest -q
```