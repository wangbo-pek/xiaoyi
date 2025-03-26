import {createApp} from 'vue'
import App from './App.vue'
import vuetify from "./plugins/vuetify";
import { createPinia } from "pinia";
import router from "./router";
import '@/styles/reset.scss'
import Particle from "@tsparticles/vue3";
import {loadFull} from "tsparticles";

const app = createApp(App)
app.use(Particle, {
    init: async (engine) => {
        await loadFull(engine)
    }
})
app.use(vuetify)
app.use(createPinia())
app.use(router)
app.mount('#app')
