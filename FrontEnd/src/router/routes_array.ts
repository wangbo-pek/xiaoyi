export const routesArray = [
    {
        path: 'home',
        name: 'home',
        component: () => import('@/views/home/Home.vue'),
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
        component: () => import('@/views/tag/Tag.vue'),
        meta: {
            title: "标签"
        }
    },
]