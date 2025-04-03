import {defineStore} from "pinia";
import cover from '@/assets/1.jpg'

const useCoverStore = defineStore('cover', {
    state: () => {
            // cover展示landing和置顶note
            let coverContents = {
                noteListId:[-1,],
                covers: [cover,],
                titles: [
                    '「 輕薄之態，施之君子，則喪吾德；施之小人，則殺吾身 」',],
                briefs: ['—— 蒲松龄',],
                buttonIcons: [
                    'mdi-atom',
                    'mdi-eye-outline',
                    'mdi-eye-outline'],
                buttonTexts: [
                    '开始',
                    '阅读',
                    '阅读']
            }
            // cover当前展示的内容
            let coverCurrentContent = {
                currentDisplayedId:coverContents.noteListId[0],
                currentDisplayedCover: coverContents.covers[0],
                currentDisplayedTitle: coverContents.titles[0],
                currentDisplayedBrief: coverContents.briefs[0],
                currentDisplayedButton: {
                    buttonIcon: coverContents.buttonIcons[0],
                    buttonText: coverContents.buttonTexts[0]
                }
            }

            return {
                coverContents,
                coverCurrentContent
            }
    }
})

export default useCoverStore