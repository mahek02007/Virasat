import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';

export default function AuthModal() {
  const {
    authModalOpen,
    authModalInitialMode,
    closeAuthModal,
    signInWithPassword,
    signUpWithPassword,
    continueAsGuest,
    isConfigured
  } = useAuth();

  const [mode, setMode] = useState('signin'); // 'signin' | 'signup'
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [errorMsg, setErrorMsg] = useState('');
  const [successMsg, setSuccessMsg] = useState('');
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    if (authModalOpen) {
      setMode(authModalInitialMode || 'signin');
      setErrorMsg('');
      setSuccessMsg('');
      setEmail('');
      setPassword('');
      setFullName('');
    }
  }, [authModalOpen, authModalInitialMode]);

  if (!authModalOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMsg('');
    setSuccessMsg('');

    if (!email.trim() || !password.trim()) {
      setErrorMsg('Please enter both email and password.');
      return;
    }

    if (mode === 'signup' && password.length < 6) {
      setErrorMsg('Password must be at least 6 characters.');
      return;
    }

    setSubmitting(true);

    try {
      if (mode === 'signin') {
        const { error } = await signInWithPassword({ email, password });
        if (error) {
          setErrorMsg(error.message || 'Failed to sign in. Please verify your credentials.');
        }
      } else {
        const { data, error } = await signUpWithPassword({
          email,
          password,
          fullName
        });
        if (error) {
          setErrorMsg(error.message || 'Failed to create account.');
        } else if (data?.user && !data?.session) {
          setSuccessMsg('Account created! Please check your email inbox to confirm your registration.');
        }
      }
    } catch (err) {
      setErrorMsg(err?.message || 'An unexpected error occurred. Please try again.');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="auth-modal-backdrop" onClick={closeAuthModal} role="dialog" aria-modal="true">
      <div
        className="auth-modal-card"
        onClick={(e) => e.stopPropagation()}
        role="document"
      >
        {/* Header */}
        <div className="auth-modal-header">
          <div className="auth-modal-brand">
            <div className="auth-brand-logo-frame">
              <img src="/assets/emblem_clean.png" alt="Virasat Emblem" className="auth-brand-emblem" />
            </div>
            <div>
              <h3 className="auth-modal-title">
                {mode === 'signin' ? 'Sign In to Virasat' : 'Create Heritage Account'}
              </h3>
              <p className="auth-modal-subtitle">
                {mode === 'signin'
                  ? 'Access your cultural journeys, badges & progress'
                  : 'Preserve your discoveries across the living heritage of Bharat'}
              </p>
            </div>
          </div>
          <button
            type="button"
            className="auth-modal-close-btn"
            onClick={closeAuthModal}
            aria-label="Close modal"
          >
            ✕
          </button>
        </div>

        {/* Tab switch */}
        <div className="auth-tabs-row" role="tablist">
          <button
            type="button"
            className={`auth-tab-btn ${mode === 'signin' ? 'active' : ''}`}
            onClick={() => {
              setMode('signin');
              setErrorMsg('');
              setSuccessMsg('');
            }}
            role="tab"
            aria-selected={mode === 'signin'}
          >
            Sign In
          </button>
          <button
            type="button"
            className={`auth-tab-btn ${mode === 'signup' ? 'active' : ''}`}
            onClick={() => {
              setMode('signup');
              setErrorMsg('');
              setSuccessMsg('');
            }}
            role="tab"
            aria-selected={mode === 'signup'}
          >
            New Account (Sign Up)
          </button>
        </div>

        {/* Not Configured Notice */}
        {!isConfigured && (
          <div className="auth-notice-banner">
            <span className="notice-icon">ℹ</span>
            <div>
              <strong>Demo/Guest Mode:</strong> Supabase environment variables (<code>VITE_SUPABASE_URL</code> & <code>VITE_SUPABASE_ANON_KEY</code>) are not yet configured in local environment. Guest exploration is active!
            </div>
          </div>
        )}

        {/* Alerts */}
        {errorMsg && (
          <div className="auth-error-alert" role="alert">
            <span className="alert-icon">⚠</span>
            <span>{errorMsg}</span>
          </div>
        )}
        {successMsg && (
          <div className="auth-success-alert" role="status">
            <span className="alert-icon">✓</span>
            <span>{successMsg}</span>
          </div>
        )}

        {/* Form */}
        <form className="auth-modal-form" onSubmit={handleSubmit}>
          {mode === 'signup' && (
            <div className="auth-input-group">
              <label htmlFor="authFullNameInput" className="auth-input-label">
                Full Name / Cultural Explorer Title
              </label>
              <input
                id="authFullNameInput"
                type="text"
                className="auth-text-input"
                placeholder="e.g. Ananya Sharma"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                autoComplete="name"
              />
            </div>
          )}

          <div className="auth-input-group">
            <label htmlFor="authEmailInput" className="auth-input-label">
              Email Address
            </label>
            <input
              id="authEmailInput"
              type="email"
              className="auth-text-input"
              placeholder="explorer@virasat.org"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              autoComplete="email"
            />
          </div>

          <div className="auth-input-group">
            <label htmlFor="authPasswordInput" className="auth-input-label">
              Password
            </label>
            <input
              id="authPasswordInput"
              type="password"
              className="auth-text-input"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              autoComplete={mode === 'signin' ? 'current-password' : 'new-password'}
              minLength={6}
            />
          </div>

          <button
            type="submit"
            className="auth-submit-btn"
            disabled={submitting}
          >
            {submitting ? (
              <span>Connecting to Virasat...</span>
            ) : mode === 'signin' ? (
              <span>Sign In to Your Journey →</span>
            ) : (
              <span>Create Account & Begin →</span>
            )}
          </button>
        </form>

        {/* Footer actions: Guest access */}
        <div className="auth-modal-footer">
          <div className="auth-guest-divider">
            <span>or continue without an account</span>
          </div>
          <button
            type="button"
            className="auth-btn-guest"
            onClick={continueAsGuest}
          >
            <span className="sparkle-icon">✦</span>
            <span>Continue as Guest Explorer (Instant Access)</span>
          </button>
        </div>
      </div>
    </div>
  );
}
