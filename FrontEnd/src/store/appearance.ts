import {defineStore} from "pinia";

const useAppearanceStore = defineStore('appearance', {
    state: () => {
        return {
            isScrollOverViewport: false,
            isShowHomeCover: true
        }
    }
})
export default useAppearanceStore
