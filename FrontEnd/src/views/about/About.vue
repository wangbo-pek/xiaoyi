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
            <div class="my-ability-text">
                <v-tabs
                    v-model="abilityTab"
                >
                    <v-tab
                        v-for="(label, index) in indicators"
                        :key="index"
                        base-color="rgb(242, 204, 15)"
                        color="rgb(242, 204, 15)"
                        slider-color="rgb(242, 204, 15)"
                    >
                        {{ label }}
                    </v-tab>
                </v-tabs>

                <v-window v-model="abilityTab" class="tab-panel-content">
                    <v-window-item v-for="(label, index) in indicators" :key="index" :value="index">
                        <div class="tab-description">
                            {{ descriptions[index] }}
                        </div>
                    </v-window-item>
                </v-window>
            </div>
        </div>

        <div class="my-skills-title">
            ——&nbsp;&nbsp;&nbsp;我的技能&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-skills">
            <div class="my-skills-progress">
                <template v-for="(item) in skills" :key="item.name">
                    <MySkillProgress :name="item.name" :level="item.degree"></MySkillProgress>
                </template>
            </div>
            <div class="my-skills-text">
                <v-tabs
                    v-model="skillTab"
                >
                    <v-tab
                        v-for="item in skills"
                        :key="item.name"
                        base-color="rgb(242, 204, 15)"
                        color="rgb(242, 204, 15)"
                        slider-color="rgb(242, 204, 15)"
                    >
                        {{ item.name }}
                    </v-tab>
                </v-tabs>

                <v-window v-model="skillTab" class="tab-panel-content">
                    <v-window-item v-for="(item, index) in skills" :key="index" :value="index">
                        <div class="tab-description">
                            {{ item.description }}
                        </div>
                    </v-window-item>
                </v-window>
            </div>
        </div>

        <div class="my-current-works-title">
            ——&nbsp;&nbsp;&nbsp;当前工作内容&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-current-works">
            <div class="flip-card" v-for="item in currentWorks" :key="item.title">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <v-icon large color="rgb(242, 204, 15)">{{ item.icon }}</v-icon>
                        <div class="card-title">{{ item.title }}</div>
                        <v-progress-linear
                            :model-value="item.currentProgress"
                            height="8"
                            color="rgb(242, 204, 15)"
                            class="card-progress"
                            rounded
                            striped
                            background-opacity="0.2"
                        ></v-progress-linear>
                        <div class="progress-label">{{ item.currentProgress }}%</div>
                    </div>
                    <div class="flip-card-back">
                        <div class="card-detail">{{ item.detail }}</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="my-todo-list-title">
            ——&nbsp;&nbsp;&nbsp;还未完成的事&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-todo-list">
            <div class="todo-item" v-for="item in todoList" :key="item.title">
                <div class="todo-icon">
                    <v-icon :icon="item.icon" size="32" color="rgb(242, 204, 15)"></v-icon>
                </div>
                <div class="todo-content">
                    <div class="todo-title-status">
                        <span class="todo-title">{{ item.title }}</span>
                        <span class="todo-status" :class="item.status">{{ item.status }}</span>
                    </div>
                    <div class="todo-description">{{ item.description }}</div>
                </div>
            </div>
        </div>

        <div class="placeholder"></div>
    </div>

    <div class="footer">
        <Footer></Footer>
    </div>
</template>

<script setup lang='ts'>
    import {onMounted, onUnmounted, ref} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";
    import useBlogStore from "@/store/blog.ts";
    import Footer from "@/components/footer/Footer.vue";
    import Header from "@/components/header/Header.vue";
    import MyAbilitiesRadar from "@/components/MyAbilitiesRadar.vue"
    import MySkillProgress from "@/components/MySkillProgress.vue"
    import {indicators, descriptions, skills, currentWorks, todoList} from '@/data/about.ts'
    import {wang} from '@/data/personalDetail.ts'

    defineOptions({
        name: 'About',
        inheritAttrs: false
    })

    let appearanceStore = useAppearanceStore()
    const blogStore = useBlogStore()
    const abilityTab = ref(0)
    const skillTab = ref(0)

    onMounted(() => {
        appearanceStore.isShowHomeCover = false
        appearanceStore.isScrollOverViewport = true
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
            margin-top: 75px;
            text-align: center;
            color: white;
            font-size: 2rem;
        }

        .my-ability {
            display: flex;
            justify-content: center;
            margin: 20px 0 20px 0;

            .my-ability-radar {
                width: 40%;
            }

            .my-ability-text {
                width: 40%;

                .tab-panel-content {
                    margin-top: 1.5rem;
                    margin-left: 1.5rem;
                }

                .tab-description {
                    font-size: 0.9rem;
                    color: white;
                    line-height: 1.5;
                }
            }
        }

        .my-skills-title {
            text-align: center;
            color: white;
            font-size: 2rem;
        }

        .my-skills {
            display: flex;
            justify-content: center;
            margin: 30px 0 30px 0;

            .my-skills-progress {
                width: 30%;
                padding: 30px;
                margin-right: 30px;
            }

            .my-skills-text {
                width: 30%;
                margin-left: 30px;

                .tab-panel-content {
                    margin-top: 1.5rem;
                    margin-left: 1.5rem;
                }

                .tab-description {
                    font-size: 0.9rem;
                    color: white;
                    line-height: 1.5;
                }
            }
        }

        .my-current-works-title {
            text-align: center;
            color: white;
            font-size: 2rem;
            margin: 30px 0 50px 0;
        }

        .my-current-works {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 2rem;
            margin: 40px auto;
            max-width: 1100px;

            .flip-card {
                background: transparent;
                width: 280px;
                height: 220px;
                perspective: 1000px;
            }

            .flip-card-inner {
                position: relative;
                width: 100%;
                height: 100%;
                transition: transform 0.6s ease-in-out;
                transform-style: preserve-3d;
                border-radius: 10px;
            }

            .flip-card:hover .flip-card-inner {
                transform: rotateY(180deg);
            }

            .flip-card-front,
            .flip-card-back {
                position: absolute;
                width: 100%;
                height: 100%;
                backface-visibility: hidden;
                background-color: rgba(0, 35, 35, 0.6);
                border: 1px solid rgba(255, 255, 255, 0.1);
                color: white;
                border-radius: 16px;
                padding: 20px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            .flip-card-front {
                .card-title {
                    margin-top: 12px;
                    font-size: 1.1rem;
                    font-weight: 600;
                    text-align: center;
                }

                .card-progress {
                    width: 80%;
                    margin-top: 1.5rem;
                }

                .progress-label {
                    margin-top: 0.25rem;
                    font-size: 0.85rem;
                    color: #ccc;
                }
            }

            .flip-card-back {
                transform: rotateY(180deg);
                font-size: 0.95rem;
                text-align: left;
                line-height: 1.6;
                padding: 1.5rem;

                .card-detail {
                    color: #f3f3f3;
                }
            }
        }

        .my-todo-list-title {
            text-align: center;
            color: white;
            font-size: 2rem;
            margin: 70px 0 50px 0;
        }

        .my-todo-list {
            max-width: 900px;
            margin: 2rem auto;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;

            .todo-item {
                display: flex;
                background-color: rgba(0, 35, 35, 0.6);
                border-radius: 16px;
                padding: 1.2rem 1.5rem;
                box-shadow: 0 2px 12px rgba(255, 255, 255, 0.05);
                transition: transform 0.3s ease;

                &:hover {
                    transform: translateY(-4px);
                }

                .todo-icon {
                    margin-right: 1.2rem;
                    display: flex;
                    align-items: start;
                }

                .todo-content {
                    flex: 1;

                    .todo-title-status {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        margin-bottom: 0.5rem;

                        .todo-title {
                            font-size: 1.1rem;
                            font-weight: 700;
                            color: white;
                        }

                        .todo-status {
                            font-size: 0.85rem;
                            padding: 4px 8px;
                            border-radius: 8px;
                            color: #fff;
                            font-weight: 600;
                        }

                        .未开始 {
                            background-color: #777;
                        }

                        .已调研 {
                            background-color: #ffa500;
                        }

                        .开发中 {
                            background-color: #2196f3;
                        }

                        .已完成 {
                            background-color: #4caf50;
                        }
                    }

                    .todo-description {
                        font-size: 0.95rem;
                        color: #ddd;
                        line-height: 1.5;
                    }
                }
            }
        }

        .placeholder {
            margin-bottom: 250px;
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

    .footer {
        width: 100%;
        min-height: 10vh;
        display: flex;
        justify-content: right;
        align-items: flex-start;
        gap: 20px;
        z-index: 900;
        background-color: white;
    }
</style>