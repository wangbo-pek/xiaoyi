import {createRouter, createWebHistory} from "vue-router";
import {routesArray} from "@/router/routes_array.ts";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/test',
            name: 'test',
            component: () => import('@/views/test.vue'),
        },
        {
            path: '/',
            name: 'layout',
            component: () => import('@/views/Layout.vue'),
            redirect: '/home',
            children: routesArray
        },
        {
            path: '/404',
            name: '404',
            component: () => import('@/views/404.vue')
        },
        {
            path: '/:pathMatch(.*)*',
            name: 'not-found',
            redirect: '/404'
        }
    ]
})

export default router