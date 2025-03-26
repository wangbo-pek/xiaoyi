<template>
    <div class="cover-area" ref="coverAreaRef">
        <transition name="fade-slide" mode="out-in">
            <div class="cover-text" :key="displayedTitle">
                <h1 class="title">{{ displayedTitle }}</h1>
                <h3 class="subtitle">{{ displayedSubtitle }}</h3>
                <v-btn class="cover-btn" variant="outlined" :prepend-icon="displayedButtonPrependIcon"
                       @click="jumpTo(displayedButtonText)">
                    {{ displayedButtonText }}
                </v-btn>
            </div>
        </transition>
        <v-img class="cover-img" :src="displayedCovers" cover></v-img>
    </div>
</template>

<script setup lang='ts'>
    import {ref, onMounted, onUnmounted} from "vue";
    import cover1 from '@/assets/1.jpg'
    import cover2 from '@/assets/2.jpg'
    import cover3 from '@/assets/3.jpg'
    import cover4 from '@/assets/4.jpg'
    import useAppearanceStore from "@/store/appearance.ts";

    defineOptions({
        name: 'Cover',
        inheritAttrs: false
    })

    const coverObject = {
        covers: [cover1, cover2, cover3, cover4],
        titles: [
            '「輕薄之態，施之君子，則喪吾德；施之小人，則殺吾身」',
            '精华一下喜欢',
            '方法记者阿萨德',
            '大学其他环境'
        ],
        subtitles: [
            ' ',
            '还是这些有限网站朋友成为.市场可是出现感觉.规定商品加入提高人民很多. 基本之后情况注册论坛工具.方式影响就是积分最新那么开始现...',
            '问题一些作者研究有限.您的点击不是开始只是最大各种.点击点击事情女人. 作为问题必须的话.学校应该个人最新觉得. 一直组织大学...',
            '免费的话一直制作成为认为一些直接.部门网络会员一些世界.需要进入日期那么地址问题技术. 精华大学那么现在一次商品其实.也是分析...',
        ],
        buttonPrependIcons: [
            'mdi-pan-down',
            'mdi-eye-outline',
            'mdi-eye-outline',
            'mdi-eye-outline',
        ],
        buttonTexts: [
            '开始',
            '阅读',
            '阅读',
            '阅读',
        ]
    }
    let displayedCovers = ref<string>('')
    let displayedTitle = ref<string>('')
    let displayedSubtitle = ref<string>('')
    let displayedButtonPrependIcon = ref<string>('')
    let displayedButtonText = ref<string>('')
    let autoSwitchCoverContent = 0
    const switchCoverContent = () => {
        displayedCovers.value = coverObject.covers[autoSwitchCoverContent]
        displayedTitle.value = coverObject.titles[autoSwitchCoverContent]
        displayedSubtitle.value = coverObject.subtitles[autoSwitchCoverContent]
        displayedButtonPrependIcon.value = coverObject.buttonPrependIcons[autoSwitchCoverContent]
        displayedButtonText.value = coverObject.buttonTexts[autoSwitchCoverContent]
        autoSwitchCoverContent++
        if (autoSwitchCoverContent > 3) {
            autoSwitchCoverContent = 0
        }
    }

    // const $router = useRouter()
    const mainContentRef = ref<HTMLElement | null>(null)
    const jumpTo = (btnText: string) => {
        if (btnText === '开始') {
            mainContentRef.value?.scrollIntoView({
                behavior: 'smooth'
            })
        }
    }

    // 获取class="cover-area"的DOM
    let coverAreaRef = ref<HTMLElement | null>(null)
    // 是否滚动过封面区域
    let appearanceStore = useAppearanceStore()

    switchCoverContent()
    setInterval(switchCoverContent, 10000)

    // 滚动监听函数
    const handleScroll = () => {
        if (coverAreaRef.value) {
            const rect = coverAreaRef.value.getBoundingClientRect()
            appearanceStore.isScrollOverViewport = rect.bottom <= 55;
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
</script>

<style scoped lang='scss'>
    .headerbar {
        padding: 0;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 5vh;
        z-index: 1000;
    }

    .cover-area {
        position: relative;
        height: 100vh;

        .cover-img {
            height: 100vh;
            filter: grayscale(80%) brightness(0.5) contrast(120%);
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
        //margin-top: 100vh;
        width: 100%;
        min-height: 90vh;
        display: flex;
        justify-content: right;
        align-items: flex-start;
        gap: 10px;
        background-color: lightseagreen;
        z-index: 900;

        .content {
            //background-color: aliceblue;
            flex: 0 0 75%;
            height: 100%;
            border-radius: 5px;
            padding: 2px 10px;
            position: relative;
            left: -50px
        }

        .siderbar {
            background-color: lightblue;
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