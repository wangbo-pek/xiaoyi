<template>
    <div class="header-container">
        <div class="header">
            <div class="title-big">
                <HeaderTitle></HeaderTitle>
            </div>
            <div class="nav-big">
                <HeaderNav></HeaderNav>
            </div>
            <div class="widget-big">
                <HeaderWidget></HeaderWidget>
            </div>
        </div>
    </div>
    <div class="coverImage" ref="coverImageRef"
         :style="{ backgroundImage: `linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.2)), url(${diaryStore.currentDiary.coverImg})`,
         filter: 'blur(1px)'}"></div>
</template>

<script setup lang='ts'>
    import {useRoute} from "vue-router";
    import {onMounted, onUnmounted, ref, watchEffect} from "vue";
    import useDiaryStore from "@/store/diary.ts";
    import axios_server from "@/utils/axios_server.ts";
    import HeaderNav from "@/components/Header/HeaderNav.vue";
    import HeaderTitle from "@/components/Header/HeaderTitle.vue";
    import HeaderWidget from "@/components/Header/HeaderWidget.vue";
    import MarkdownIt from "markdown-it";
    import hljs from "highlight.js";
    import 'highlight.js/styles/github.css'

    defineOptions({
        name: 'DiaryDetail',
        inheritAttrs: false
    })

    const route = useRoute()
    const diaryStore = useDiaryStore()
    const diaryListId = Number(route.params.id)
    const md = new MarkdownIt({html: true})

    let coverImageRef = ref<HTMLElement | null>(null)
    let isScrollOverViewport = ref(false)
    const handleScroll = () => {
        if (coverImageRef.value) {
            let rect = coverImageRef.value.getBoundingClientRect()
            isScrollOverViewport.value = rect.bottom <= 55
        }
    }

    // 解析并高亮代码块
    const highlightCode = () => {
        const codeBlock = document.querySelectorAll('pre code')
        codeBlock.forEach((block) => {
            hljs.highlightElement(block as HTMLElement)
        })
    }

    onMounted(async () => {
        // 页面加载时，从后端获取日记content
        const result = await axios_server.get('', {
            params: {
                diaryListId
            }
        })
        Object.assign(diaryStore.currentDiary, result.data)

        // 将markdown进行渲染
        diaryStore.currentDiary.renderedMarkdown = md.render(diaryStore.currentDiary.markdownContent)
        // 调用highlightCode处理代码高亮
        highlightCode()

        // 监听handleScroll
        window.addEventListener('scroll', handleScroll)
        const rect = coverImageRef.value!.getBoundingClientRect()
        isScrollOverViewport.value = rect.bottom <= 55
    })

    onUnmounted(() => {
        window.removeEventListener('scroll', handleScroll)
    })

    // 实时渲染markdown
    watchEffect(() => {
        if (diaryStore.currentDiary.renderedMarkdown) {
            setTimeout(() => {
                highlightCode()
            }, 100)
        }
    })
</script>

<style scoped lang='scss'>
    .header-container {
        padding: 0;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 5vh;
        z-index: 1000;

        .header {
            display: flex;
            justify-content: center;
            align-items: stretch;
            height: 100%;
            width: 100%;
            background-color: rgba(100, 100, 100, 0.5);

            .title-big {
                width: 35%;
                height: 100%;
                padding-right: 30px;
            }

            .nav-big {
                width: 35%;
                height: 100%;
            }

            .widget-big {
                width: 30%;
                height: 100%;
            }
        }

        .change-bgcolor {
            background-color: #113c46;
        }
    }

    .coverImage {
        width: 100%;
        height: 50vh;
        background-size: cover;
        background-position: top center;
        background-repeat: no-repeat;
        background-position-x: 10%;
        background-position-y: 50%;
        filter: brightness(0.5);
    }
</style>