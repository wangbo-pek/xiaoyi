import {createRouter, createWebHistory} from "vue-router";
import {routesArray} from "@/router/routes_array.ts";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'layout',
            component: () => import('@/views/Layout.vue'),
            redirect: '/home',
            children: routesArray
        },
        {
            path: '/note/detail/:id',
            name: 'noteDetail',
            component: () => import('@/views/NoteDetail.vue'),
            meta: {
                title: "笔记内容"
            }
        },
        {
            path: '/diary/detail/:id',
            name: 'diaryDetail',
            component: () => import('@/views/DiaryDetail.vue'),
            meta: {
                title: "日记内容"
            }
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