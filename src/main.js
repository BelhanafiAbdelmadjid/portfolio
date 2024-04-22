import { createApp } from 'vue'
import App from './App.vue'
import VueSmoothScroll from 'vue3-smooth-scroll'
import { createMemoryHistory, createRouter } from 'vue-router'
import landingPage from "./views/landing-page.vue"
const routes = [
    { path: '/', component: landingPage },
    { path: '/*', component: landingPage },
  ]

const router = createRouter({
    history: createMemoryHistory(),
    routes,
  })

const app = createApp(App)
app.use(VueSmoothScroll)
app.use(router)
app.mount('#app')


