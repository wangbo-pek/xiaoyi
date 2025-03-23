import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from "vite-plugin-vuetify";

// https://vite.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        vuetify()
    ],
    css: {
        preprocessorOptions: {
            scss: {
                // 自动引入
                additionalData: `
                @import "@/styles/_variables.scss";
                @import "@/styles/_mixins.scss";
                `
            }
        }
    }
})
