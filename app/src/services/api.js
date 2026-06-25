const BASE_URL = import.meta.env.VITE_API_URL

async function request(path, options = {}) {
  const res = await fetch(`${BASE_URL}${path}`, {
    credentials: 'include',
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  })

  const data = await res.json().catch(() => ({}))

  if (!res.ok) {
    const message =
      data?.errors?.[0]?.detail ||
      (res.status === 401 ? 'E-mail ou senha incorretos.' : `Erro ${res.status}`)
    throw new Error(message)
  }

  return data
}

export function register({ nome, email, password }) {
  return request('/auth/register', {
    method: 'POST',
    body: JSON.stringify({ nome, email, password }),
  })
}

export function login({ email, password }) {
  return request('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  })
}

export function logout() {
  return request('/auth/logout', { method: 'POST' })
}
