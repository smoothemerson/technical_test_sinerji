# Frontend

Interface React + Vite com autenticação JWT em memória.

## Pré-requisitos

- Docker e Docker Compose instalados.
- O backend rodando e acessível (por padrão `http://localhost:3000`).

## Variáveis de ambiente obrigatórias

| Variável       | Descrição                                      | Exemplo                      |
|----------------|------------------------------------------------|------------------------------|
| `VITE_API_URL` | URL base do backend, **sem** barra final       | `http://localhost:3000`      |

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

Edite `.env` (ou exporte a variável antes de subir o compose):

```bash
VITE_API_URL=https://api.meudominio.com docker compose up --build
```

## Rotas disponíveis

| Rota          | Descrição                                          |
|---------------|----------------------------------------------------|
| `/register`   | Cadastro — nome, e-mail e senha (≥ 8 caracteres)   |
| `/login`      | Login — e-mail e senha                             |
| `/dashboard`  | Rota protegida — redireciona para `/login` se não autenticado |

## Observações de segurança

- O JWT é armazenado **exclusivamente em memória** (React Context + variável de módulo).
- Nunca é escrito em `localStorage`, `sessionStorage` ou cookies.
- Enviado via header `Authorization: Bearer <token>` em todas as requisições autenticadas.
- Ao recarregar a página o token é perdido e o usuário precisa fazer login novamente — comportamento intencional.
