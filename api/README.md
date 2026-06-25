# API — JWT Authentication

REST API em **FastAPI** com autenticação JWT e persistência em **PostgreSQL**.

---

## Requisitos

| Ferramenta | Versão mínima |
|---|---|
| Python | 3.13+ |
| PostgreSQL | 14+ |
| [uv](https://docs.astral.sh/uv/) | qualquer |
| Docker + Docker Compose | opcional |

---

## Setup local (sem Docker)

### 1. Clone e entre na pasta
```bash
git clone https://github.com/smoothemerson/technical_test_sinerji.git
cd technical_test_sinerji/api
```

### 2. Configure as variáveis de ambiente
```bash
cp .env.example .env
```

Edite `.env` com suas credenciais:
```env
KEY=sua_chave_secreta_jwt          # chave para assinar os tokens
ALGORITHM=HS256
JWT_HOURS=10
POSTGRES_USER=postgres_user
POSTGRES_PASS=postgres_pass
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=postgres
```

### 3. Instale as dependências
```bash
uv sync
```

### 4. Inicie o servidor
```bash
uv run python run.py
```

A API estará disponível em `http://localhost:3000`.  
Documentação interativa (Swagger): `http://localhost:3000/docs`

---

## Setup com Docker Compose

Sobe PostgreSQL + API de uma vez:

```bash
# Na raiz do repositório
docker compose up --build
```

| Serviço | URL |
|---|---|
| API | http://localhost:3000 |
| Swagger | http://localhost:3000/docs |

> O schema SQL é aplicado automaticamente no primeiro `docker compose up`.

---

## Testes

```bash
# Rodar todos os testes
uv run pytest

# Com relatório de cobertura
uv run pytest --cov
```

---

## Estrutura do projeto

```
api/
├── init/
│   └── schema.sql          # DDL da tabela users
├── src/
│   ├── configs/            # Configurações (JWT)
│   ├── controllers/        # Regras de negócio + testes
│   ├── drivers/            # JWT handler, password handler + testes
│   ├── errors/             # Tipos de erro HTTP
│   ├── main/
│   │   ├── composer/       # Injeção de dependência
│   │   ├── middlewares/    # Verificação JWT
│   │   ├── routes/         # Rotas FastAPI
│   │   └── server/         # App FastAPI
│   ├── models/
│   │   ├── interface/      # Interfaces do repositório
│   │   ├── repositories/   # Acesso ao banco + testes
│   │   └── settings/       # Conexão PostgreSQL
│   └── views/              # Camada HTTP (request/response) + testes
├── .env.example
├── Dockerfile
├── pyproject.toml
└── run.py
```
