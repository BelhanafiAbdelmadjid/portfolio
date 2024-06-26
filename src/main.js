import { createApp } from 'vue'
import App from './App.vue'
import VueSmoothScroll from 'vue3-smooth-scroll'
import { createWebHistory, createRouter } from 'vue-router'
import landingPage from "./views/landing-page.vue"
import aboutMe from "./views/about-me.vue"
const routes = [
    { path: '/', component: landingPage },
    { path: '/about', component: aboutMe },
    { path: '/404', component: landingPage },  
    { path: "/:catchAll(.*)", redirect: '/' },  
  
  ]

const router = createRouter({
    history: createWebHistory("/"),
    routes,
    scrollBehavior() {
      // always scroll to top
      return { top: 0 }
    },
  })

const app = createApp(App)
app.use(router)
app.use(VueSmoothScroll)
app.mount('#app')


