import {defineStore} from "pinia";
import type {DiaryListItem} from "@/store/types/diary.ts";

export const useDiaryStore = defineStore('diary', {
    state: () => {
        return {
            diaryList: [] as DiaryListItem[],
            currentDiaryList: {
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
                '#1c1965',
                '#421b73',
                '#61197e',
                '#8a197b',
                '#8a1948',
                '#8a1919',
                '#8a3b19',
                '#8a5d19',
                '#8a7319',
                '#7f8a19',
                '#508a19',
                '#198a1b',
                '#198a5f',
            ]
        }
    }
})