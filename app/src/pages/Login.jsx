import { useState } from 'react'
import { useNavigate, Link, useLocation } from 'react-router-dom'
import { login as apiLogin } from '../services/api.js'
import { useAuth } from '../contexts/AuthContext.jsx'
import styles from './Auth.module.css'

export default function Login() {
  const navigate = useNavigate()
  const location = useLocation()
  const { login } = useAuth()
  const [fields, setFields] = useState({ email: '', password: '' })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const justRegistered = location.state?.registered

  function handleChange(e) {
    setFields((f) => ({ ...f, [e.target.name]: e.target.value }))
  }

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')
    setLoading(true)
    try {
      await apiLogin(fields)
      login()
      navigate('/dashboard', { replace: true })
    } catch (err) {
      setError(err.message || 'E-mail ou senha incorretos.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className={styles.page}>
      <form className={styles.card} onSubmit={handleSubmit} noValidate>
        <h1 className={styles.title}>Entrar</h1>

        {justRegistered && (
          <p className={styles.success}>Conta criada com sucesso! Faça login.</p>
        )}
        {error && <p className={styles.error} role="alert">{error}</p>}

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
          autoComplete="current-password"
          value={fields.password}
          onChange={handleChange}
          required
        />

        <button className={styles.button} type="submit" disabled={loading}>
          {loading ? 'Entrando…' : 'Entrar'}
        </button>

        <p className={styles.footer}>
          Não tem conta?{' '}
          <Link className={styles.link} to="/register">Cadastre-se</Link>
        </p>
      </form>
    </div>
  )
}
