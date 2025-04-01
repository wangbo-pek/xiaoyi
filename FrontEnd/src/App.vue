<template>
    <v-app>
        <router-view></router-view>
    </v-app>
</template>

<script setup lang='ts'>
    import {onMounted} from "vue";
    import useNoteStore from "@/store/note.ts";
    import useDiaryStore from "@/store/diary.ts";
    import axios_server from "./utils/axios_server.ts";

    defineOptions({
        name: 'App',
        inheritAttrs: false
    })

    let noteStore = useNoteStore()
    let diaryStore = useDiaryStore()

    onMounted(() => {
        // 每次App.vue加载，都会发送请求，设置csrf_token
        axios_server.get('csrf/').then(() => {
            // 每次App.vue加载，都会发送请求，获取Note文章列表信息
            axios_server.get('getAllNoteList/').then(
                (response) => {
                    // 把文章列表信息保存到noteStore仓库中
                    noteStore.noteList = response.data
                    console.log('>>>> noteStore.noteList <<<<')
                    console.log(noteStore.noteList)
                }
            )
            axios_server.get('getAllDiaryList/').then(
                (response) => {
                    // 把文章列表信息保存到diaryStore仓库中
                    diaryStore.diaryList = response.data
                    diaryStore.diaryList.forEach((value) => {
                        value.timelinePointColor = diaryStore.timelinePointColor[Math.floor(Math.random() * diaryStore.timelinePointColor.length)]
                    })
                    console.log('>>>> diaryStore.diaryList <<<<')
                    console.log(diaryStore.diaryList)
                }
            )
        })
    })
</script>

<style lang="scss">
    body {
        background-color: #113c46;
    }
</style>