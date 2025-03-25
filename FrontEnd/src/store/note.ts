import {defineStore} from "pinia";
import type NoteListItem from "@/store/types/note.ts";

const useNoteStore = defineStore('note', {
    state: () => {
        return {
            noteList: [] as NoteListItem[]
        }
    }
})
export default useNoteStore
