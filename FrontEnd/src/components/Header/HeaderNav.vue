<template>
    <div class="nav-container">
        <v-btn variant="text" class="my-btn" @click="jumpTo('note')">笔记</v-btn>
        <v-btn variant="text" class="my-btn" @click="jumpTo('essay')">文章</v-btn>
        <v-btn variant="text" class="my-btn" @click="jumpTo('diary')">日记</v-btn>
        <v-btn variant="text" class="my-btn" @click="jumpTo('tags')">标签</v-btn>
    </div>
</template>

<script setup lang='ts'>
    import {useRouter} from "vue-router";

    defineOptions({
        name: 'HeaderNav',
        inheritAttrs: false
    })

    const $router = useRouter()
    const jumpTo = (path: string) => {
        $router.push(path)

    }

</script>

<style scoped lang='scss'>
    .nav-container {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-end;

        .my-btn {
            width: 50px;
            font-size: 14px;
            font-weight: 900;
            color: white;
            //margin: 0 5px;
            //background-color: rgba(255, 255, 255, 0.15)
        }
    }
</style>
