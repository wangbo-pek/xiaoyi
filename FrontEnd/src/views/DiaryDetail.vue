<template>
    <div class="header-container">
        <div class="header" :class="{'change-bgcolor':isScrollOverViewport}">
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

    <div class="title-container">
        <span class="diary-title">{{ diaryStore.currentDiary.title }}</span>
    </div>

    <div class="content-container">
        <div class="diary-background">
            <div class="diary-created-time">
                <v-icon class="created-date-icon" icon="mdi-calendar-sync-outline"></v-icon>
                <span class="created-date-text">{{ diaryStore.currentDiary.createdTime }}</span>
            </div>

            <div class="body-container">
                <div class="diary-body markdown-content" v-html="diaryStore.currentDiary.renderedMarkdown"></div>
            </div>
        </div>
    </div>

    <div class="coffee-container">
        <span class="coffee-text">COFFEE ME &nbsp;</span>
        <v-img class="coffee-icon"
               :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/coffee.svg'"></v-img>
    </div>

    <div class="divider3"></div>

</template>

<script setup lang='ts'>
    import {useRoute} from "vue-router";
    import {onMounted, onUnmounted, ref, watchEffect} from "vue";
    import useDiaryStore from "@/store/diary.ts";
    import axios_server from "@/utils/axios_server.ts";
    import HeaderNav from "@/components/header/HeaderNav.vue";
    import HeaderTitle from "@/components/header/HeaderTitle.vue";
    import HeaderWidget from "@/components/header/HeaderWidget.vue";
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
        const result = await axios_server.get('getDiaryAllContent/', {
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
        height: 10vh;
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
            background-color: #071417;
            box-shadow: 5px 0 10px rgba(255, 255, 255, 0.5);
            border-bottom: 1px solid rgba(255, 255, 255, 0.5);
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

    .title-container {
        .diary-title {
            padding: 5px 15px 5px 200px;
            border-radius: 3px 6px 9px 12px;
            position: relative;
            top: -2rem;
            left: 20rem;
            font-size: 1.3rem;
            background-color: rgba(7, 20, 23, 0.75);
            color: #cccccc;
        }
    }

    .content-container {
        display: flex;
        justify-content: center;
        align-items: flex-start;

        .diary-background {
            padding: 50px 80px 20px 80px;
            width: 75%;
            position: relative;
            top: -3em;

            .diary-created-time {
                display: flex;
                align-items: center;
                gap: 4px;

                .created-date-icon {
                    color: #8ab9a8;
                    font-size: 1rem;
                }

                .created-date-text {
                    color: #8ab9a8;
                    font-size: 1rem;
                }
            }

            .body-container {
                display: flex;
                justify-content: center;
                align-items: flex-start;

                .diary-body {
                    width: 100%;
                    padding: 15px 25px;
                    border-radius: 12px;
                }
            }
        }


    }

    .coffee-container {
        position: relative;
        top: -10px;
        display: flex;
        justify-content: center;
        align-items: center;

        .coffee-icon {
            max-width: 2.5%;
        }

        .coffee-text {
            color: #c3effa;
            font-size: 1rem;
            font-weight: 800;
        }
    }

    .divider3 {
        position: relative;
        top: -2px;
        display: flex;
        width: 100%;
        height: 2px;
        background-color: #515c7a;;
        margin: 50px 0 100px 0;
    }

    @import "@/styles/markdown";
    :deep(.markdown-content) {
    }

    :deep(.toc) {
    }
</style>