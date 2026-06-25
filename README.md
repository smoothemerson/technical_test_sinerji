# Setup

**Pré-requisitos:** Docker e Docker Compose.

## Subindo tudo

```bash
git clone https://github.com/smoothemerson/technical_test_sinerji.git
cd technical_test_sinerji
docker compose up --build
```

| Serviço | URL |
|---|---|
| Frontend | http://localhost:5173 |
| API | http://localhost:3000 |
| Docs (Swagger) | http://localhost:3000/docs |

## Variáveis de ambiente

O compose já inclui valores padrão funcionais. Para sobrescrever, crie um `.env` na raiz:

```env
KEY=sua_chave_secreta_jwt
```

## Partes desenvolvidas com auxílio de IA

As seguintes entregas foram geradas com assistência do **Claude (Anthropic)**:

- **`app/`** — frontend completo (React + Vite): estrutura de arquivos, roteamento, contexto de autenticação JWT em memória, páginas de login/cadastro/dashboard, CSS Modules e Dockerfile.
- **`.github/workflows/ci.yml`** — pipeline de CI com dois jobs: testes do backend via `pytest` e verificação de build do frontend via Vite.

O código do backend (`api/`) foi desenvolvido manualmente.
