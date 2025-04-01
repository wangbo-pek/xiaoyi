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
            timelinePointColor: [
                'rgba(106,164,59,0.5)',
                'rgba(41,138,161,0.5)',
                'rgba(138,51,182,0.5)',
                'rgba(182,90,51,0.5)',
            ]
        }
    }
})

export default useDiaryStore