<template>
    <div class="title-container">
        <div class="title">
            <v-btn variant="text" class="my-btn" @click="jumpTo">
                XiaoYi_Blog
            </v-btn>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import {useRouter} from "vue-router";

    defineOptions({
        name: 'HeaderTitle',
        inheritAttrs: false
    })


    const $router = useRouter()
    const jumpTo = () => {
        $router.push({
            name: 'home'
        })
    }
</script>

<style scoped lang='scss'>
    .title-container {
        height: 100%;

        .title {
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            margin-right: 25px;

            .my-btn {
                width: 120px;
                font-size: 14px;
                font-weight: 900;
                color: white;
                text-transform: none;
                //margin: 0 5px;
                //background-color: rgba(255, 255, 255, 0.15)
            }
        }
    }
</style>