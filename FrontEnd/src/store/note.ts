import {defineStore} from "pinia";
import type {NoteListItem} from "@/store/types/note.ts";

const useNoteStore = defineStore('note', {
    state: () => {
        return {
            noteList: [] as NoteListItem[],
            currentNote: {
                "noteListId": 0,
                "title": '',
                "brief": '',
                "coverImg": '',
                "isShow": false,
                "isPinned": false,
                "isRecommended": false,
                "viewedCount": 0,
                "likedCount": 0,
                "disgustedCount": 0,
                "encouragedCount": 0,
                "createdTime": '',
                "modifiedTime": '',
                "tagsName": [],
                "category": '',
                "markdownContent": '',
                "htmlContent": '',
                "imageUrls": [],
                "renderedMarkdown": '',
                "tableOfContent":''
            },
            recommendedNoteList: [] as NoteListItem[],
            latestNoteList: [] as NoteListItem[]
        }
    }
})
export default useNoteStore