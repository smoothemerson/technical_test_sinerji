# Frontend

Interface React + Vite com autenticação via cookie HTTP-only gerenciado pelo backend.

## Pré-requisitos

- Docker e Docker Compose instalados.
- O backend rodando e acessível (por padrão `http://localhost:3000`).

## Variáveis de ambiente obrigatórias

| Variável       | Descrição                                | Exemplo                 |
|----------------|------------------------------------------|-------------------------|
| `VITE_API_URL` | URL base do backend, **sem** barra final | `http://localhost:3000` |

Copie `.env.example` para `.env` e preencha o valor:

```bash
cp .env.example .env
```

## Como rodar

```bash
# A partir da pasta app/
docker compose up --build
```

O Vite dev server ficará disponível em **http://localhost:5173**.

## Apontando para outro backend

```bash
VITE_API_URL=https://api.meudominio.com docker compose up --build
```

## Rotas disponíveis

| Rota         | Descrição                                                     |
|--------------|---------------------------------------------------------------|
| `/register`  | Cadastro — nome, e-mail e senha (≥ 8 caracteres)             |
| `/login`     | Login — e-mail e senha                                        |
| `/dashboard` | Rota protegida — redireciona para `/login` se não autenticado |

## Autenticação

O token JWT é gerenciado inteiramente pelo backend via **cookie HTTP-only**:

- O frontend nunca acessa o token diretamente.
- O browser envia o cookie automaticamente em todas as requisições com `credentials: 'include'`.
- O logout chama `POST /auth/logout` no backend, que apaga o cookie.
- Protegido contra XSS (cookie inacessível ao JavaScript) e CSRF (cookie `SameSite=Strict`).
