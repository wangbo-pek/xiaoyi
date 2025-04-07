import {defineStore} from "pinia";
import type {BlogInformation} from "@/store/types/blog.ts";

const useBlogStore = defineStore('blog', {
    state: () => {
        return {
            blogInfo: {
                "blogName": '',
                "myName": '',
                "myMotto": '',
                "myWisdom": '',
                "myLocation": '',
                "myCareer": '',
                "myShortIntro": '',
                "myFormalIntro": '',
                "blogArticlesCount": 0,
                "blogWordsCount": 0,
                "blogViewedCount":0,
                "blogDurationRunning": 0,
                "myWechat": '',
                "myMain": '',
                "coffeeByWechat": '',
                "coffeeByAlipay": ''
            } as BlogInformation
        }
    }
})

export default useBlogStore