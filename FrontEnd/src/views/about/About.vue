<template>
    <div class="header">
        <Header></Header>
    </div>
    <div class="about-container">
        <div class="my-avatar">
            <v-img class="my-avatar-icon"
                   :src="wang.avatar"></v-img>
        </div>
        <div class="my-name">
            <span class="my-name-text">{{ wang.nickName }}</span>
        </div>

        <div class="my-formal-intro">
            <div class="my-formal-intro-text">
                {{ wang.longIntro }}
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

        <div class="my-ability-title">
            ——&nbsp;&nbsp;&nbsp;我的能力&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-ability">
            <div class="my-ability-radar">
                <MyAbilitiesRadar></MyAbilitiesRadar>
            </div>
            <div class="my-skills-progress">
                <template v-for="(item) in skills" :key="item.name">
                    <MySkillProgress :name="item.name" :level="item.degree"></MySkillProgress>
                </template>
            </div>
        </div>

        <div class="my-current-works-title">
            ——&nbsp;&nbsp;&nbsp;我的任务&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-current-works">
            <div class="my-current-works-item" v-for="item in currentWorks" :key="item.title">
                <div class="my-current-works-content">
                    <div class="my-current-works-title-status">
                        <span class="my-current-works-titles">{{ item.title }}</span>
                        <span class="my-current-works-status" :class="item.status">{{ item.status }}</span>
                    </div>
                    <div class="my-current-works-description">{{ item.description }}</div>
                    <v-progress-linear
                        :model-value="item.currentProgress"
                        height="8"
                        color="rgb(242, 204, 15)"
                        class="current-progress"
                        rounded
                        striped
                        background-opacity="0.2"
                    ></v-progress-linear>
                </div>
            </div>
        </div>

        <div class="placeholder"></div>
    </div>

</template>

<script setup lang='ts'>
    import {onMounted, onUnmounted} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";
    import Header from "@/components/header/Header.vue";
    import MyAbilitiesRadar from "@/components/MyAbilitiesRadar.vue"
    import MySkillProgress from "@/components/MySkillProgress.vue"
    import {skills, currentWorks} from '@/data/about.ts'
    import {wang} from '@/data/personalDetail.ts'

    defineOptions({
        name: 'About',
        inheritAttrs: false
    })

    let appearanceStore = useAppearanceStore()

    onMounted(() => {
        appearanceStore.isShowHomeCover = false
        appearanceStore.isScrollOverViewport = true

        window.scrollTo({
            top: 0,
            behavior: 'smooth' // 可选，平滑滚动
        })
    })

    onUnmounted(() => {
        appearanceStore.isShowHomeCover = true
    })

</script>

<style scoped lang='scss'>
    .header {
        padding: 0;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 8vh;
        z-index: 1000;
    }

    .about-container {
        position: relative;
        top: 10rem;

        .my-avatar {
            display: flex;
            justify-content: center;

            .my-avatar-icon {
                max-width: 12rem;
            }
        }

        .my-name {
            margin: 20px 0 20px 0;
            display: flex;
            justify-content: center;

            .my-name-text {
                color: white;
                font-size: 2rem;
                font-weight: 200;
            }
        }

        .my-formal-intro {
            display: flex;
            justify-content: center;
            margin: 10px 0 30px 0;

            .my-formal-intro-text {
                color: white;
                max-width: 50rem;
                font-size: 1rem;
                font-weight: 700;
                text-align: left;
                line-height: 30px;
            }
        }

        .touch-me {
            position: relative;
            width: 100%;
            display: flex;
            justify-content: center;

            .wechat-icon {
                margin: 0 20px 0 20px;
                max-width: 2rem;
            }

            .mail-icon {
                margin: 0 20px 0 20px;
                max-width: 2rem;
            }

            .twitter-icon {
                margin: 0 20px 0 20px;
                max-width: 2rem;
            }
        }

        .my-ability-title {
            margin: 100px 0 30px 0;
            text-align: center;
            color: white;
            font-size: 1.75rem;
        }

        .my-ability {
            display: flex;
            justify-content: center;
            margin: 20px auto;

            .my-ability-radar {
                width: 40%;
            }

            .my-skills-progress {
                width: 40%;
                padding-top: 65px;
                padding-left: 150px;
            }

        }

        .my-current-works-title {
            text-align: center;
            color: white;
            font-size: 1.75rem;
            margin: 50px 0 30px 0;
        }

        .my-current-works {
            max-width: 750px;
            margin: 2rem auto;
            display: flex;
            flex-direction: column;
            gap: 2.5rem;

            .my-current-works-item {
                display: flex;
                background-color: rgba(0, 35, 35, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 16px;
                padding: 1.2rem 1.5rem;
                transition: transform 0.3s ease;

                &:hover {
                    transform: translateY(-4px);
                }

                .my-current-works-content {
                    flex: 1;

                    .my-current-works-title-status {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        margin-bottom: 0.5rem;

                        .my-current-works-titles {
                            font-size: 1.1rem;
                            font-weight: 700;
                            color: white;
                        }

                        .my-current-works-status {
                            font-size: 0.85rem;
                            padding: 4px 8px;
                            border-radius: 8px;
                            color: #fff;
                            font-weight: 600;
                        }

                        .未开始 {
                            background-color: #777;
                        }

                        .准备中 {
                            background-color: #ffa500;
                        }

                        .进行中 {
                            background-color: #2196f3;
                        }

                        .已完成 {
                            background-color: #4caf50;
                        }
                    }

                    .my-current-works-description {
                        font-size: 0.95rem;
                        color: #ddd;
                        line-height: 1.5;
                    }

                    .current-progress {
                        margin-top: 1rem;
                        width: 100%;
                    }
                }
            }
        }

        .placeholder {
            margin-bottom: 75px;
        }
    }

    :deep(.v-slide-group__prev),
    :deep(.v-slide-group__next) {
        color: rgb(242, 204, 15);
        opacity: 0.6;

        &:hover {
            opacity: 1;
        }
    }

    :deep(.v-tab) {
        text-transform: none !important;
    }

</style>