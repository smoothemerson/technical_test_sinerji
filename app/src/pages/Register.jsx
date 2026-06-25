import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { register } from '../services/api.js'
import styles from './Auth.module.css'

function validate({ nome, email, password }) {
  if (!nome.trim()) return 'O nome é obrigatório.'
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailRegex.test(email)) return 'Informe um e-mail válido.'
  if (password.length < 8) return 'A senha deve ter no mínimo 8 caracteres.'
  return null
}

export default function Register() {
  const navigate = useNavigate()
  const [fields, setFields] = useState({ nome: '', email: '', password: '' })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  function handleChange(e) {
    setFields((f) => ({ ...f, [e.target.name]: e.target.value }))
  }

  async function handleSubmit(e) {
    e.preventDefault()
    const validationError = validate(fields)
    if (validationError) {
      setError(validationError)
      return
    }
    setError('')
    setLoading(true)
    try {
      await register(fields)
      navigate('/login', { state: { registered: true } })
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className={styles.page}>
      <form className={styles.card} onSubmit={handleSubmit} noValidate>
        <h1 className={styles.title}>Criar conta</h1>

        {error && <p className={styles.error} role="alert">{error}</p>}

        <label className={styles.label} htmlFor="nome">Nome</label>
        <input
          className={styles.input}
          id="nome"
          name="nome"
          type="text"
          autoComplete="name"
          value={fields.nome}
          onChange={handleChange}
          required
        />

        <label className={styles.label} htmlFor="email">E-mail</label>
        <input
          className={styles.input}
          id="email"
          name="email"
          type="email"
          autoComplete="email"
          value={fields.email}
          onChange={handleChange}
          required
        />

        <label className={styles.label} htmlFor="password">Senha</label>
        <input
          className={styles.input}
          id="password"
          name="password"
          type="password"
          autoComplete="new-password"
          value={fields.password}
          onChange={handleChange}
          required
        />

        <button className={styles.button} type="submit" disabled={loading}>
          {loading ? 'Cadastrando…' : 'Cadastrar'}
        </button>

        <p className={styles.footer}>
          Já tem conta?{' '}
          <Link className={styles.link} to="/login">Entrar</Link>
        </p>
      </form>
    </div>
  )
}
