import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), 'VITE_');
  const apiTarget = new URL(env.VITE_API_BASE_URL || 'http://127.0.0.1:8000');

  // localhost may resolve to IPv6 while a local Uvicorn process listens only
  // on IPv4. Normalize this local alias for the dev proxy connection.
  if (apiTarget.hostname === 'localhost') apiTarget.hostname = '127.0.0.1';

  return {
    plugins: [react()],
    server: {
      proxy: {
        '/api': {
          target: apiTarget.origin,
          changeOrigin: true,
        },
      },
    },
  };
});
