import {defineStore} from "pinia";
import type {CategoryCount} from "@/store/types/category.ts";

const useCategoriesStore = defineStore('categories', {
    state: () => {
        return {
            categoryStats:[] as CategoryCount[]
        }
    }
})

export default useCategoriesStore