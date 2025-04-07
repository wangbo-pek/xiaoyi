<template>
    <div class="title-container">
        <div class="my-avatar">
            <v-img class="my-avatar-icon"
                   :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/my_only_girl.png'"></v-img>
        </div>

        <div class="title">
            <v-btn variant="text" class="my-btn" @click="jumpTo">
                {{ blogStore.blogInfo.blogName }}
            </v-btn>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import {useRouter} from "vue-router";
    import useBlogStore from "@/store/blog.ts";

    defineOptions({
        name: 'HeaderTitle',
        inheritAttrs: false
    })

    const blogStore = useBlogStore()
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
        display: flex;
        justify-content: center;

        .my-avatar {
            height: 100%;
            width: 50%;
            display: flex;
            justify-content: flex-end;

            .my-avatar-icon {
                max-width: 1.5rem;
            }
        }

        .title {
            height: 100%;
            width: 22%;
            display: flex;
            align-items: center;
            justify-content: flex-end;

            .my-btn {
                width: 120px;
                font-size: 14px;
                font-weight: 900;
                color: white;
                text-transform: none;
            }
        }
    }
</style>