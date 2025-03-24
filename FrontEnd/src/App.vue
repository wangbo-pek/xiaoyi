<template>
    <v-app>
        <!-- 页面的顶部：包括了博客名称、导航菜单(笔记、文章、日记、关于我)、其他小挂件(天气、日历)-->
        <div class="header">
            <Header></Header>
        </div>
        <!-- 页面内容展示区：左侧(宽)笔记、文章、日记的列表、展示右侧(窄) -->
        <div class="content">
            <router-view></router-view>
        </div>

    </v-app>
</template>

<script setup lang='ts'>
    // import {onMounted} from "vue";
    // import axios_server from "./utils/axios_server.ts";
    import Header from "@/components/Header/Header.vue";

    defineOptions({
        name: 'App',
        inheritAttrs: false
    })

    // onMounted(() => {
    //     // 每次App.vue加载，都会发送请求，设置csrf_token
    //     axios_server.get('/csrf/')
    // })
</script>

<style scoped lang="scss">
    .header {
        padding: 0;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 10vh;
        z-index: 1000;
        background-image: linear-gradient(to right, #0388e7, #2bbbfa, #1cf3fa, #08fad6);
    }

    .content {
        padding: 0;
        margin: 0;
        position: fixed;
        top: 10vh;
        left: 0;
        width: 100%;
        height: 90vh;
        z-index: 1000;
    }
</style>