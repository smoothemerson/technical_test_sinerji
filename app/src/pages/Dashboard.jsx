import { useNavigate } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext.jsx'
import { logout as apiLogout } from '../services/api.js'
import styles from './Dashboard.module.css'

export default function Dashboard() {
  const navigate = useNavigate()
  const { logout } = useAuth()

  async function handleLogout() {
    await apiLogout().catch(() => {})
    logout()
    navigate('/login', { replace: true })
  }

  return (
    <div className={styles.page}>
      <div className={styles.card}>
        <h1 className={styles.title}>Dashboard</h1>
        <p className={styles.subtitle}>Você está autenticado.</p>
        <button className={styles.button} onClick={handleLogout}>Sair</button>
      </div>
    </div>
  )
}
