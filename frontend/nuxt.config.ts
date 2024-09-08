// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  routeRules: {
    '/': { ssr: false } //ログイン画面 - CSR
  },
  runtimeConfig: {
    public: {
      baseURL: 'http://localhost:8000', //Django REST Framework接続
    },
  },
})
