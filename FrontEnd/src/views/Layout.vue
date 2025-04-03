<template>
    <!-- 页面的顶部：包括了博客名称、导航菜单(笔记、文章、日记、标签)-->
    <div class="header">
        <Header></Header>
    </div>

    <!-- 首页展示的大图 -->
    <Cover v-if="appearanceStore.isShowHomeCover" @jump-to="handleJump"></Cover>

    <!-- 页面内容展示区：左侧(宽)笔记、文章、日记的列表、展示右侧(窄) -->
    <div class="main" ref="mainContentRef">
        <div class="content">
            <router-view></router-view>
        </div>
        <div class="sider">
            <Sider></Sider>
        </div>
    </div>

    <!-- 展示页面的footer -->
    <div class="footer">
        <Footer></Footer>
    </div>
</template>

<script setup lang='ts'>
    import Header from "@/components/header/Header.vue";
    import Sider from "@/components/sider/Sider.vue";
    import Footer from "@/components/footer/Footer.vue";
    import Cover from "@/components/Cover.vue";
    import useAppearanceStore from "@/store/appearance.ts";
    import {nextTick, ref} from "vue";

    defineOptions({
        name: 'Layout',
        inheritAttrs: false
    })

    const appearanceStore = useAppearanceStore()
    const mainContentRef = ref<HTMLElement | null>(null)
    const handleJump = async (noteListId: number) => {
        if (noteListId === -1 && mainContentRef.value) {
            await nextTick()
            const offsetTop = mainContentRef.value.offsetTop

            window.scrollTo({
                top: offsetTop - 50,
                behavior: "smooth"
            })
        }
    }

</script>

<style scoped lang="scss">
    .header {
        padding: 0;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 8vh;
        z-index: 1000;
    }

    .main {
        width: 100%;
        min-height: 90vh;
        display: flex;
        justify-content: right;
        align-items: flex-start;
        gap: 20px;
        z-index: 900;

        .content {
            flex: 0 0 75%;
            height: 100%;
            border-radius: 5px;
            padding: 2px 10px;
            position: relative;
            left: 1rem
        }

        .sider {
            flex: 0 0 25%;
            height: 100%;
            padding: 10px;
            overflow-y: auto;
            position: relative;
            left: -1rem;
        }
    }

    .footer {
        width: 100%;
        min-height: 10vh;
        display: flex;
        justify-content: right;
        align-items: flex-start;
        gap: 20px;
        z-index: 900;
        background-color: white;
    }
</style>