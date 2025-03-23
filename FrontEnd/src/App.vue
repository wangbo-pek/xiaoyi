<template>
    <v-app>
        <!-- 页面的顶部：包括了博客名称、导航菜单(笔记、文章、日记、关于我)、其他小挂件(天气、日历)-->
        <v-container>
            <v-row>
                <v-col cols="12"></v-col>
            </v-row>
        </v-container>
        <!-- 页面内容展示区：左侧(宽)笔记、文章、日记的列表、展示右侧(窄) -->
        <v-container>
            <router-view></router-view>
        </v-container>
    </v-app>
</template>

<script setup lang='ts'>
    // import {onMounted} from "vue";
    // import axios_server from "./utils/axios_server.ts";
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

</style>