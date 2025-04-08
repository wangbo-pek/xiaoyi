<template>
    <div class="nav-container">
        <v-btn variant="text" class="my-btn" density="compact" prepend-icon="" @click="jumpTo('note')"><v-icon>mdi-fountain-pen-tip</v-icon>笔记</v-btn>
        <v-btn variant="text" class="my-btn" density="compact" @click="jumpTo('diary')"><v-icon>mdi-ghost</v-icon>日记</v-btn>
        <v-btn variant="text" class="my-btn" density="compact" @click="jumpTo('tags')"><v-icon>mdi-tag-multiple</v-icon>标签</v-btn>
        <v-btn variant="text" class="my-btn" density="compact" @click="jumpTo('about')"><v-icon>mdi-creation-outline</v-icon>关于我</v-btn>
    </div>
</template>

<script setup lang='ts'>
    import {useRouter} from "vue-router";

    defineOptions({
        name: 'HeaderNav',
        inheritAttrs: false
    })

    const $router = useRouter()
    const jumpTo = (name: string) => {
        $router.push({
            name
        })
    }

</script>

<style scoped lang='scss'>
    .nav-container {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-end;

        .my-btn {
            width: 75px;
            font-size: 14px;
            font-weight: 900;
            color: white;
            margin: 0 5px;
        }
    }
</style>
