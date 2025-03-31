<template>
    <!-- 页面的顶部：包括了博客名称、导航菜单(笔记、文章、日记、标签)-->
    <div class="headerbar">
        <Header></Header>
    </div>

    <!-- 首页展示的大图 -->
    <Cover v-if="appearanceStore.isShowHomeCover"></Cover>

    <!-- 页面内容展示区：左侧(宽)笔记、文章、日记的列表、展示右侧(窄) -->
    <div class="main" ref="mainContentRef">
        <div class="content">
            <router-view></router-view>
        </div>
        <div class="siderbar">
            <Sider></Sider>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import Header from "@/components/Header/Header.vue";
    import Sider from "@/components/Sider/Sider.vue";
    import Cover from "@/components/Cover.vue";
    import useAppearanceStore from "@/store/appearance.ts";

    defineOptions({
        name: 'Layout',
        inheritAttrs: false
    })

    const appearanceStore = useAppearanceStore()

</script>

<style scoped lang="scss">
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
            background-color: rgba(255, 0, 0, 0.15);
            height: 100%;
            border-radius: 5px;
            padding: 2px 10px;
            position: relative;
            left: -1.5rem
        }

        .siderbar {
            background-image: linear-gradient(to top,
            rgba(17, 60, 70, 0.01),
            rgba(17, 60, 70, 0.05),
            rgba(17, 60, 70, 0.10),
            rgba(17, 60, 70, 0.15),
            rgba(17, 60, 70, 0.20),
            rgba(17, 60, 70, 0.25),
            rgba(17, 60, 70, 0.30),
            rgba(17, 60, 70, 0.35),
            rgba(17, 60, 70, 0.4),
            rgba(17, 60, 70, 0.45),
            rgba(17, 60, 70, 0.5),
            rgba(17, 60, 70, 0.55),
            rgba(17, 60, 70, 0.6),
            rgba(17, 60, 70, 0.65),
            rgba(17, 60, 70, 0.7),
            rgba(17, 60, 70, 0.75),
            rgba(17, 60, 70, 0.8),
            rgba(17, 60, 70, 0.85),
            rgba(17, 60, 70, 0.9),
            rgba(17, 60, 70, 0.95),
            rgba(17, 60, 70, 1)
            );
            flex: 0 0 20%;
            height: 100%;
            padding: 10px;
            overflow-y: auto;
            position: relative;
            left: -0.15rem;
        }
    }
</style>