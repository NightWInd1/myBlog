import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig(({ command }) => ({
  base: command === 'serve' ? '/' : '/static/',
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
    port: 3000,
    proxy: {
      '/api': 'http://127.0.0.1:8000',
      '/feed': 'http://127.0.0.1:8000',
      '/admin': 'http://127.0.0.1:8000',
      '/static/admin': 'http://127.0.0.1:8000',
    },
  },
  build: {
    outDir: '../static',
    emptyOutDir: true,
  },
}))
