import {createApp} from 'vue'
import App from './App.vue'
import vuetify from "./plugins/vuetify";
import { createPinia } from "pinia";
import router from "./router";
// 引入全局的清除默认样式文件
import '@/styles/reset.scss'


const app = createApp(App)
app.use(vuetify)
app.use(createPinia())
app.use(router)
app.mount('#app')
