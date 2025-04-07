import {defineStore} from "pinia";
import cover from '@/assets/1.jpg'

const useCoverStore = defineStore('cover', {
    state: () => {
            // cover展示landing和置顶note
            let coverContents = {
                noteListId:[-1,],
                covers: [cover,],
                titles: [
                    '欢迎来到一只产品狗的小天地，博客简陋，照顾不周，望请海涵。',],
                briefs: [' —— Wang (北京)',],
                buttonIcons: [
                    'mdi-menu-down',
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