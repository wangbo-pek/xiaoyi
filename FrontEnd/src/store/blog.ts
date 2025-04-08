import {defineStore} from "pinia";
import type {BlogInformation} from "@/store/types/blog.ts";

const useBlogStore = defineStore('blog', {
    state: () => {
        return {
            blogInfo: {
                "blogName": '',
                "blogArticlesCount": 0,
                "blogWordsCount": 0,
                "blogViewedCount":0,
                "blogDurationRunning": 0,
            } as BlogInformation
        }
    }
})

export default useBlogStore