import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './styles.css';
import { AuthProvider } from './context/AuthContext';
import AuthModal from './components/AuthModal';
import LandingPage from './pages/LandingPage';
import AtlasPage from './pages/AtlasPage';
import RegionPage from './pages/RegionPage';

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/atlas" element={<AtlasPage />} />
          <Route path="/regions/:regionId" element={<RegionPage />} />
        </Routes>
        <AuthModal />
      </BrowserRouter>
    </AuthProvider>
  </React.StrictMode>
);