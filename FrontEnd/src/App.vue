<template>
    <v-app>
        <!-- 页面的顶部：包括了博客名称、导航菜单(笔记、文章、日记、关于我)、其他小挂件(天气、日历)-->
        <div class="headerbar">
            <Header></Header>
        </div>
        <!-- 页面内容展示区：左侧(宽)笔记、文章、日记的列表、展示右侧(窄) -->
        <div class="main">
            <div class="content">
                <router-view></router-view>
            </div>
            <div class="siderbar">
                <div>siderbar</div>
            </div>

        </div>

    </v-app>
</template>

<script setup lang='ts'>
    import {onMounted} from "vue";
    import axios_server from "./utils/axios_server.ts";
    import Header from "@/components/Header/Header.vue";

    defineOptions({
        name: 'App',
        inheritAttrs: false
    })


    onMounted(() => {
        // 每次App.vue加载，都会发送请求，设置csrf_token
        axios_server.get('/csrf/')
    })
</script>

<style scoped lang="scss">
    .headerbar {
        padding: 0;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 10vh;
        z-index: 1000;
        background-image: linear-gradient(to right, #34a4f5, #43e1fc, #66f6d5, #65f8ae);
    }

    .main {
        position: fixed;
        top: 10vh;
        left: 0;
        width: 100%;
        height: 90vh;
        z-index: 900;
        display: flex;
        justify-content: right;
        align-items: flex-start;
        gap: 10px;
        margin-top:2px;

        .content {
            background-color: aliceblue;
            flex: 0 0 70%;
            height: 100%;
            border-radius: 5px;
            padding: 2px 10px;
            overflow-y: auto;
        }

        .siderbar {
            background-color: lightblue;
            flex: 0 0 20%;
            height: 100%;
            border-radius: 5px;
            padding: 10px;
            overflow-y: auto;
        }
    }
</style>