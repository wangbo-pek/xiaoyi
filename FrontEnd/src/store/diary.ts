import {defineStore} from "pinia";
import type {DiaryListItem} from "@/store/types/diary.ts";

const useDiaryStore = defineStore('diary', {
    state: () => {
        return {
            diaryList: [] as DiaryListItem[],
            currentDiary: {
                "diaryListId": 0,
                "title": '',
                "brief": '',
                "coverImg": '',
                "isShow": false,
                "viewedCount": 0,
                "createdTime": '',
                "modifiedTime": '',
                "markdownContent": '',
                "htmlContent": '',
                "imageUrls": [],
                "renderedMarkdown": ''
            },
            timelineColors: [
                {pointColor: 'rgba(231,156,115,0.2)', textColor: 'rgba(231,156,115,0.8)'},
                {pointColor: 'rgba(200,229,115,0.2)', textColor: 'rgba(200,229,115,0.8)'},
                {pointColor: 'rgba(113,224,131,0.2)', textColor: 'rgba(113,224,131,0.8)'},
                {pointColor: 'rgba(113,198,229,0.2)', textColor: 'rgba(113,198,229,0.8)'},
                {pointColor: 'rgba(177,113,229,0.2)', textColor: 'rgba(177,113,229,0.8)'},
                {pointColor: 'rgba(229,113,157,0.2)', textColor: 'rgba(229,113,157,0.8)'}
            ]
        }
    }
})

export default useDiaryStore