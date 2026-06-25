const BASE_URL = import.meta.env.VITE_API_URL

async function request(path, options = {}) {
  const res = await fetch(`${BASE_URL}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  })

  const data = await res.json().catch(() => ({}))

  if (!res.ok) {
    const message =
      data?.message ||
      data?.error ||
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

export function authedRequest(path, getToken, options = {}) {
  const token = getToken()
  return request(path, {
    ...options,
    headers: {
      ...options.headers,
      Authorization: `Bearer ${token}`,
    },
  })
}
