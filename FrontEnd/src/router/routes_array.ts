export const routesArray = [
    {
        path: 'home',
        name: 'home',
        component: () => import('@/views/Home/Home.vue'),
        meta: {
            title: '首页'
        }
    },
    {
        path: 'note',
        name: 'note',
        component: () => import('@/views/note/Note.vue'),
        meta: {
            title: "笔记"
        }
    },
    {
        path: 'essay',
        name: 'essay',
        component: () => import('@/views/essay/Essay.vue'),
        meta: {
            title: "文章"
        }
    },
    {
        path: 'diary',
        name: 'diary',
        component: () => import('@/views/diary/Diary.vue'),
        meta: {
            title: "日记"
        }
    },
    {
        path: 'tags',
        name: 'tags',
        component: () => import('@/views/about/About.vue'),
        meta: {
            title: "标签"
        }
    },
]