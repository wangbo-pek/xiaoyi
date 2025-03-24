<template>
    <div class="nav-container">
        <template v-for="item in routesArray" :key="item.path">
            <v-btn variant="text" class="my-btn" @click="jumpTo(item.name)">{{ item.meta.title }}</v-btn>
        </template>
    </div>
</template>

<script setup lang='ts'>
    import {routesArray} from "@/router/routes_array.ts";
    import {useRouter} from "vue-router";

    defineOptions({
        name: 'HeaderNavBig',
        inheritAttrs: false
    })

    const $router = useRouter()

    const jumpTo = (path:string) => {
        $router.push(path)
    }
</script>

<style scoped lang='scss'>
    .nav-container {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: space-evenly;

        .my-btn {
            width: 100px;
            font-size: 18px;
            color: #262323;
            margin: 0 10px;
            background-color: rgba(255, 255, 255, 0.15)
        }
    }
</style>
