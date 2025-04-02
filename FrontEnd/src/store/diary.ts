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
                {pointColor: 'rgba(230,150,120,0.25)', textColor: 'rgba(230,150,120,0.75)'},
                {pointColor: 'rgba(200,230,120,0.25)', textColor: 'rgba(200,230,120,0.75)'},
                {pointColor: 'rgba(120,220,130,0.25)', textColor: 'rgba(120,220,130,0.75)'},
                {pointColor: 'rgba(110, 200,230,0.25)', textColor: 'rgba(110, 200,230,0.75)'},
                {pointColor: 'rgba(180,110,230,0.25)', textColor: 'rgba(180,110,230,0.75)'},
                {pointColor: 'rgba(230,110,160,0.25)', textColor: 'rgba(230,110,160,0.75)'}
            ]
        }
    }
})

export default useDiaryStore