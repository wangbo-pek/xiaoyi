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
            axios_server.get('getNoteList/').then(
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

</style>