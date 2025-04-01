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
                '#3ba48c',
                '#298aa1',
                '#3370b6',
            ]
        }
    }
})

export default useDiaryStore