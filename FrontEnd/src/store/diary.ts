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
                '#1c4948',
                '#0f3554',
                '#61197e',
                '#8a1948',
                '#8a1919',
                '#8a3b19',
                '#8a5d19',
                '#7f8a19',
                '#198a1b',
                '#198a5f',
            ]
        }
    }
})

export default useDiaryStore