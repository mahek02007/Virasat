import { useState, useRef, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';

export default function UserProfileMenu() {
  const { user, isGuest, signOut, openAuthModal } = useAuth();
  const [menuOpen, setMenuOpen] = useState(false);
  const containerRef = useRef(null);

  useEffect(() => {
    const handleClickOutside = (e) => {
      if (containerRef.current && !containerRef.current.contains(e.target)) {
        setMenuOpen(false);
      }
    };
    document.addEventListener('click', handleClickOutside);
    return () => document.removeEventListener('click', handleClickOutside);
  }, []);

  const fullName = user?.user_metadata?.full_name || user?.email?.split('@')[0] || 'Explorer';
  const initials = isGuest
    ? 'GE'
    : fullName
        .split(' ')
        .map((n) => n[0])
        .join('')
        .slice(0, 2)
        .toUpperCase() || 'EX';

  return (
    <div className="profile-menu-container" ref={containerRef} id="profileMenuContainer">
      <button
        type="button"
        className="profile-btn"
        id="profileToggleBtn"
        aria-label="Open Explorer Profile"
        aria-expanded={menuOpen}
        onClick={() => setMenuOpen((prev) => !prev)}
      >
        <div className={`profile-avatar-circle ${!isGuest ? 'signed-in' : ''}`}>{initials}</div>
        <div className="profile-label-group">
          <span className="profile-name">{isGuest ? 'Guest Explorer' : fullName}</span>
          <span className="profile-role-badge">
            {isGuest ? 'Level 1 • Novice' : 'Living Heritage Explorer'}
          </span>
        </div>
        <svg viewBox="0 0 20 20" width="14" height="14" fill="currentColor" style={{ opacity: 0.7 }}>
          <path
            fillRule="evenodd"
            d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
            clipRule="evenodd"
          />
        </svg>
      </button>

      <div className={`profile-dropdown-menu ${menuOpen ? 'active' : ''}`} id="profileDropdown">
        <div className="profile-header-card">
          <span className="profile-h-title">Cultural Pass</span>
          <span className="profile-h-sub">
            {isGuest ? 'Guest Explorer Account' : user?.email}
          </span>
        </div>

        <div className="profile-stats-row">
          <div className="profile-stat-box">
            <span className="profile-stat-val">3</span>
            <span className="profile-stat-lbl">Explored</span>
          </div>
          <div className="profile-stat-box">
            <span className="profile-stat-val">3</span>
            <span className="profile-stat-lbl">Badges</span>
          </div>
          <div className="profile-stat-box">
            <span className="profile-stat-val">43%</span>
            <span className="profile-stat-lbl">Journey</span>
          </div>
        </div>

        {isGuest ? (
          <button
            type="button"
            className="btn-profile-signin"
            id="profileDropdownSignInBtn"
            onClick={() => {
              setMenuOpen(false);
              openAuthModal('signin');
            }}
          >
            Sign In to Save Permanent Progress
          </button>
        ) : (
          <div className="profile-auth-actions">
            <div className="profile-user-status">
              <span className="status-dot-active" />
              <span>Session Synced via Supabase</span>
            </div>
            <button
              type="button"
              className="btn-profile-signout"
              id="profileDropdownSignOutBtn"
              onClick={async () => {
                setMenuOpen(false);
                await signOut();
              }}
            >
              Sign Out
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
