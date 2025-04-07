<template>
    <div class="header">
        <Header></Header>
    </div>
    <div class="about-container">
        <div class="my-avatar">
            <v-img class="my-avatar-icon"
                   :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/my_only_girl.png'"></v-img>
        </div>
        <div class="my-name">
            <span class="my-name-text">Wang</span>
        </div>
        <div class="what-i-wanna-say">
            <div class="what-i-wanna-say-text">
                人的一生就应该像一条河，开始是涓涓细流，被狭窄的河岸所束缚，然后，它激烈地奔过巨石，冲越瀑布。渐渐地，河流变宽了，两边的堤岸也远去，河水流动得更加平静。最后，它自然地融入了大海，并毫无痛苦地消失了自我。
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
                    v-model="activeTab"
                >
                    <v-tab
                        v-for="(label, index) in myAbilitiesIndicators"
                        :key="index"
                        base-color="rgb(255, 152, 0)"
                        color="rgb(255, 152, 0)"
                        slider-color="rgb(255, 152, 0)"
                    >
                        {{ label }}
                    </v-tab>
                </v-tabs>

                <v-window v-model="activeTab" class="tab-panel-content">
                    <v-window-item v-for="(label, index) in myAbilitiesIndicators" :key="index" :value="index">
                        <div class="tab-description">
                            {{ myAbilitiesDescriptions[index] }}
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
                <template v-for="(item) in mySkills" :key="item.name">
                    <MySkillProgress :name="item.name" :level="item.degree"></MySkillProgress>
                </template>
            </div>
            <div class="my-skills-text">
                <v-tabs
                    v-model="activeTab"
                >
                    <v-tab
                        v-for="item in mySkills"
                        :key="item.name"
                        base-color="rgb(255, 152, 0)"
                        color="rgb(255, 152, 0)"
                        slider-color="rgb(255, 152, 0)"
                    >
                        {{ item.name }}
                    </v-tab>
                </v-tabs>

                <v-window v-model="activeTab" class="tab-panel-content">
                    <v-window-item v-for="(item, index) in mySkills" :key="index" :value="index">
                        <div class="tab-description">
                            {{ item.description }}
                        </div>
                    </v-window-item>
                </v-window>
            </div>
        </div>

        <div class="my-other-title">
            ——&nbsp;&nbsp;&nbsp;我的其他&nbsp;&nbsp;&nbsp;——
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
    import Footer from "@/components/footer/Footer.vue";
    import Header from "@/components/header/Header.vue";
    import MyAbilitiesRadar from "@/components/MyAbilitiesRadar.vue"
    import MySkillProgress from "@/components/MySkillProgress.vue";

    defineOptions({
        name: 'About',
        inheritAttrs: false
    })

    let appearanceStore = useAppearanceStore()
    const activeTab = ref(0)
    const myAbilitiesDescriptions = [
        '善于从宏观把握市场变化，能洞察业务逻辑并挖掘潜在价值。',
        '熟悉敏捷开发流程，能够协调多方资源高效推进项目。',
        '能够结构化地收集、分析和管理用户需求，保障产品方向准确。',
        '具备编程能力，能深入理解技术实现，协助技术方案制定。',
        '注重沟通与团队协作，同时具备较强的时间与情绪管理能力。'
    ]
    const myAbilitiesIndicators = [
        '市场理解和商业洞察',
        '敏捷开发和项目管理',
        '需求分析和需求管理',
        '编程开发和技术积累',
        '沟通协作和自我管理'
    ]


    const mySkills = [
        {
            name: 'Axure',
            degree: 93,
            description: '111善于从宏观把握市场变化，能洞察业务逻辑并挖掘潜在价值。'
        },
        {
            name: 'Python',
            degree: 75,
            description: '善于从宏观把握市场变化，能洞察业务逻辑并挖掘潜在价值。'
        },
        {
            name: '数据分析',
            degree: 70,
            description: '善于从宏观把握市场变化，能洞察业务逻辑并挖掘潜在价值。'
        },
        {
            name: 'JavaScript',
            degree: 66,
            description: '善于从宏观把握市场变化，能洞察业务逻辑并挖掘潜在价值。'
        },
    ]

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

        .what-i-wanna-say {
            display: flex;
            justify-content: center;
            margin: 10px 0 30px 0;

            .what-i-wanna-say-text {
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
                max-width: 2.5rem;
            }

            .mail-icon {
                margin: 0 20px 0 20px;
                max-width: 2.5rem;
            }

            .twitter-icon {
                margin: 0 20px 0 20px;
                max-width: 2.5rem;
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
            margin: 20px 0 100px 0;

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

        .my-other-title {
            text-align: center;
            color: white;
            font-size: 2rem;
        }

        .placeholder {
            margin-bottom: 300px;
        }
    }

    :deep(.v-slide-group__prev),
    :deep(.v-slide-group__next) {
        color: #ff9800;
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