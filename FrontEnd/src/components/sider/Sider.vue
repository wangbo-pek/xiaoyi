<template>
    <div class="sider-container">
        <div class="introduction" @click="jumpToAbout">
            <div class="my-avatar">
                <v-img class="my-avatar-icon"
                       :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/my_only_girl.png'"></v-img>
            </div>
            <div class="my-name">
                <span class="my-name-text">{{ blogStore.blogInfo.myName }}</span>
            </div>

            <div class="my-short-intro">
                <div class="my-short-intro-text">
                    {{ blogStore.blogInfo.myShortIntro }}
                </div>
            </div>


        </div>
        <div class="touch-me">
            <v-img class="wechat-icon"
                   :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/wechat.svg'"></v-img>
            <v-img class="mail-icon"
                   :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/gmail.svg'"></v-img>
            <v-img class="twitter-icon"
                   :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/twitter.svg'"></v-img>
        </div>
        <div class="coffee-container">
            <span class="coffee-text">COFFEE ME &nbsp;</span>
            <v-img class="coffee-icon"
                   :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/coffee.svg'"></v-img>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import {useRouter} from "vue-router";
    import useBlogStore from "@/store/blog.ts";

    defineOptions({
        name: 'Sider',
        inheritAttrs: false
    })

    const $router = useRouter()
    const blogStore = useBlogStore()

    const jumpToAbout = () => {
        $router.push({
            name: 'about',
        })
    }


</script>

<style scoped lang='scss'>
    .sider-container {
        position: relative;
        width: 100%;
        height: 100%;

        .introduction {
            text-align: center;
            position: relative;
            top: 5rem;
            width: 100%;
            cursor: pointer;

            .my-avatar {
                display: flex;
                justify-content: center;

                .my-avatar-icon {
                    max-width: 5rem;
                }
            }

            .my-name {
                margin: 10px 0 10px 0;

                .my-name-text {
                    color: white;
                    font-size: 1.5rem;
                    font-weight: 200;
                }
            }

            .my-short-intro {
                display: flex;
                justify-content: center;
                margin: 10px 0 10px 0;

                .my-short-intro-text {
                    color: white;
                    max-width: 15rem;
                    font-size: 0.8rem;
                    font-weight: 700;
                    text-align: left;
                    line-height: 20px;
                }
            }


        }

        .touch-me {
            position: relative;
            top: 5.5rem;
            width: 100%;
            display: flex;
            justify-content: center;
            margin-top: 20px;

            .wechat-icon {
                margin: 0 15px 0 15px;
                max-width: 1.8rem;
            }

            .mail-icon {
                margin: 0 15px 0 15px;
                max-width: 1.8rem;
            }

            .twitter-icon {
                margin: 0 15px 0 15px;
                max-width: 1.8rem;
            }
        }

        .coffee-container {
            position: relative;
            top: 7.5rem;
            display: flex;
            justify-content: center;
            align-items: center;

            .coffee-icon {
                max-width: 10%;
            }

            .coffee-text {
                color: rgb(0, 200, 250);
                font-size: 1rem;
                font-weight: 800;
            }
        }
    }
</style>