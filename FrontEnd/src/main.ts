import {createApp} from 'vue'
import App from './App.vue'
import vuetify from "./plugins/vuetify";
import { createPinia } from "pinia";
import router from "./router";
import '@/styles/reset.scss'
import Vue3Particles from "vue3-particles"

const app = createApp(App)
app.use(vuetify)
app.use(createPinia())
app.use(router)
app.use(Vue3Particles)
app.mount('#app')
