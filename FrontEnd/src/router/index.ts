import {createRouter, createWebHistory} from "vue-router";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/test',
            name: 'test',
            component: () => import('@/views/test.vue')
        },
        {
            path: '/',
            redirect: '/layout/home'
        },
        {
            path: '/layout',
            name: 'layout',
            component: () => import('@/views/Layout.vue'),
            redirect: '/layout/home',
            children: [
                {
                    path: 'home',
                    name: 'home',
                    component: () => import('@/views/home/Home.vue')
                },
                {
                    path: 'note',
                    name: 'note',
                    component: () => import('@/views/note/Note.vue')
                },
                {
                    path: 'essay',
                    name: 'essay',
                    component: () => import('@/views/essay/Essay.vue')
                },
                {
                    path: 'diary',
                    name: 'diary',
                    component: () => import('@/views/diary/Diary.vue')
                },
                {
                    path: 'about',
                    name: 'about',
                    component: () => import('@/views/about/About.vue')
                },
            ]
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