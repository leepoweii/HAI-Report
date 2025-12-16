// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  modules: ['@nuxtjs/tailwindcss'],

  // SPA mode - no SSR needed for this project
  ssr: false,

  app: {
    head: {
      title: 'HAI Virtual Exhibition',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Human-Robot Interaction Virtual Exhibition' }
      ],
      htmlAttrs: {
        class: 'dark'
      }
    }
  },

  // Runtime config for API URL
  runtimeConfig: {
    public: {
      apiUrl: process.env.NUXT_PUBLIC_API_URL || 'http://localhost:8000'
    }
  },

  // Tailwind CSS config
  tailwindcss: {
    cssPath: '~/assets/css/main.css',
    configPath: 'tailwind.config.ts'
  }
})
