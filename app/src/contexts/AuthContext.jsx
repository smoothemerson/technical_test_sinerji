import { createContext, useContext, useState, useCallback } from 'react'

const AuthContext = createContext(null)

// Token lives exclusively in module memory — never touches localStorage/sessionStorage
let _token = null

export function AuthProvider({ children }) {
  const [isAuthenticated, setIsAuthenticated] = useState(false)

  const login = useCallback((token) => {
    _token = token
    setIsAuthenticated(true)
  }, [])

  const logout = useCallback(() => {
    _token = null
    setIsAuthenticated(false)
  }, [])

  const getToken = useCallback(() => _token, [])

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout, getToken }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used inside AuthProvider')
  return ctx
}
