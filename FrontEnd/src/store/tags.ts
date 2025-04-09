import {defineStore} from "pinia";
import type {TagCount} from "@/store/types/tag.ts";

const useTagsStore = defineStore('tags', {
    state: () => {
        return {
            tagStats:[] as TagCount[]
        }
    }
})

export default useTagsStore