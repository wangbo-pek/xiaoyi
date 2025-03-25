<template>
    <v-app>
        <router-view></router-view>
    </v-app>
</template>

<script setup lang='ts'>
    import {onMounted} from "vue";
    import useNoteStore from "@/store/note.ts";
    import axios_server from "./utils/axios_server.ts";


    defineOptions({
        name: 'App',
        inheritAttrs: false
    })

    let noteStore = useNoteStore()

    onMounted(() => {
        // 每次App.vue加载，都会发送请求，设置csrf_token
        axios_server.get('csrf/').then(() => {
            // 每次App.vue加载，都会发送请求，获取Note文章列表信息
            axios_server.get('getArticleList/').then(
                (response) => {
                    // 把文章列表信息保存到noteStore仓库中
                    noteStore.noteList = response.data
                    console.log('noteStore.noteList')
                    console.log(noteStore.noteList)
                }
            )
        })
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
        margin-top: 2px;

        .content {
            //background-color: aliceblue;
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