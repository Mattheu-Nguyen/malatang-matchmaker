import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  build: {
    rollupOptions: {
      output: {
        // Hash-only names — no spaces/parentheses in URLs (avoids 404 on Vercel / Flask)
        assetFileNames: 'assets/[hash][extname]',
      },
    },
  },
  server: {
    proxy: {
      // Local Flask: python backend/app.py — same path as production /recommend rewrite
      '/recommend': { target: 'http://127.0.0.1:5000', changeOrigin: true },
    },
  },
})
