<template>
    <router-view></router-view>
</template>

<script setup lang='ts'>
    import {onMounted} from "vue";
    import axios_server from "./utils/axios_server.ts";
    defineOptions({
        name: 'App',
        inheritAttrs: false
    })

    onMounted(() => {
        // 每次App.vue加载，都会发送请求，设置csrf_token
        axios_server.get('/csrf/')
    })
</script>

<style scoped>

</style>