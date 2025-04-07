<template>
    <div class="cover-area" ref="coverAreaRef">
        <transition name="fade-slide" mode="out-in">
            <div class="cover-text" :key="coverStore.coverCurrentContent.currentDisplayedTitle">
                <h1 class="title">{{ coverStore.coverCurrentContent.currentDisplayedTitle }}</h1>
                <h3 class="subtitle">{{ coverStore.coverCurrentContent.currentDisplayedBrief }}</h3>
                <v-btn class="cover-btn" variant="outlined"
                       :prepend-icon="coverStore.coverCurrentContent.currentDisplayedButton.buttonIcon"
                       @click="jumpTo(coverStore.coverCurrentContent.currentDisplayedId)">
                    {{ coverStore.coverCurrentContent.currentDisplayedButton.buttonText }}
                </v-btn>
            </div>
        </transition>
        <v-img class="cover-img" :src="coverStore.coverCurrentContent.currentDisplayedCover" cover></v-img>
    </div>
</template>

<script setup lang='ts'>
    import {ref, onMounted, onUnmounted, watch} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";
    import useNoteStore from "@/store/note.ts";
    import useCoverStore from "@/store/cover.ts";
    import {useRouter} from "vue-router";

    defineOptions({
        name: 'Cover',
        inheritAttrs: false
    })

    const emit = defineEmits<{
        (e: 'jump-to', noteListId: number): void
    }>()

    let noteStore = useNoteStore()
    let coverStore = useCoverStore()
    const $router = useRouter()

    let currentContentIndex = 0
    const switchCoverContent = () => {
        coverStore.coverCurrentContent.currentDisplayedId = coverStore.coverContents.noteListId[currentContentIndex]
        coverStore.coverCurrentContent.currentDisplayedCover = coverStore.coverContents.covers[currentContentIndex]
        coverStore.coverCurrentContent.currentDisplayedTitle = coverStore.coverContents.titles[currentContentIndex]
        coverStore.coverCurrentContent.currentDisplayedBrief = coverStore.coverContents.briefs[currentContentIndex]
        coverStore.coverCurrentContent.currentDisplayedButton.buttonIcon = coverStore.coverContents.buttonIcons[currentContentIndex]
        coverStore.coverCurrentContent.currentDisplayedButton.buttonText = coverStore.coverContents.buttonTexts[currentContentIndex]
        currentContentIndex++
        if (currentContentIndex > 2) {
            currentContentIndex = 0
        }
    }

    const jumpTo = (noteListId: number) => {
        if (noteListId === -1) {
            emit('jump-to', noteListId)
        } else {
            $router.push({
                name: 'noteDetail',
                params: {
                    id: noteListId
                }
            })
        }
    }

    // 获取class="cover-area"的DOM
    let coverAreaRef = ref<HTMLElement | null>(null)
    // 是否滚动过封面区域
    let appearanceStore = useAppearanceStore()

    // 滚动监听函数
    const handleScroll = () => {
        if (coverAreaRef.value) {
            const rect = coverAreaRef.value.getBoundingClientRect()
            appearanceStore.isScrollOverViewport = rect.bottom <= 300;
        }
    }

    // 页面挂载时监听滚动事件
    onMounted(() => {
        window.addEventListener('scroll', handleScroll)
        const rect = coverAreaRef.value!.getBoundingClientRect()
        appearanceStore.isScrollOverViewport = rect.bottom <= 55;

    })

    // 页面卸载时移除监听
    onUnmounted(() => {
        window.removeEventListener('scroll', handleScroll)
    })

    // 监听App.vue是否拿到了NoteList，如果拿到了，就获取被置顶的文章
    watch(() => noteStore.noteList, () => {
        const result = noteStore.noteList.filter((value) => {
            return value.isPinned === true
        })
        result.forEach((value) => {
            coverStore.coverContents.noteListId.push(value.noteListId)
            coverStore.coverContents.covers.push(value.coverImg)
            coverStore.coverContents.titles.push(value.title)
            coverStore.coverContents.briefs.push(value.brief)
        })
        console.log(coverStore.coverContents)
        switchCoverContent()
        setInterval(switchCoverContent, 10000)
    })

</script>

<style scoped lang='scss'>
    .cover-area {
        position: relative;
        height: 100vh;

        .cover-img {
            height: 100vh;
            filter: grayscale(80%) brightness(0.7) contrast(120%);
        }

        .cover-text {
            position: absolute;
            top: 45%;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
            z-index: 2;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.6);
        }

        .title {
            font-size: 30px;
            white-space: nowrap;
            color: white;
            min-height: 3.2rem;
        }

        .subtitle {
            font-size: 20px;
            color: white;
            min-height: 1rem;
            max-width: 30vw;
            margin: 0 auto;
            white-space: normal;
            word-break: break-word;
            line-height: 1.6;
        }

        .cover-btn {
            margin-top: 150px;
            font-weight: bold;
            font-size: 16px;
            color: white;
        }

        // 默认：淡入 + 上下滑动
        .fade-slide-enter-active,
        .fade-slide-leave-active {
            transition: all 0.4s ease;
        }

        .fade-slide-enter-from {
            opacity: 0;
            transform: translateY(20px);
        }

        .fade-slide-leave-to {
            opacity: 0;
            transform: translateY(-20px);
        }

        @keyframes blink {
            from, to {
                opacity: 1;
            }
            50% {
                opacity: 0;
            }
        }
    }

    .main {
        width: 100%;
        min-height: 90vh;
        display: flex;
        justify-content: right;
        align-items: flex-start;
        gap: 10px;
        z-index: 900;

        .content {
            flex: 0 0 75%;
            height: 100%;
            border-radius: 5px;
            padding: 2px 10px;
            position: relative;
            left: -50px
        }

        .siderbar {
            flex: 0 0 15%;
            height: 100%;
            border-radius: 5px;
            padding: 10px;
            overflow-y: auto;
            position: relative;
            left: -5px
        }
    }
</style>