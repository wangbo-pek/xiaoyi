<template>
    <div class="card-container" :style="{backgroundImage:`url(${bgImage})`}">
        <div class="overlay">
            <div class="text-container">
                <!-- title -->
                <h2 class="title-text">{{ title }}</h2>
                <!-- subtitle -->
                <p class="subtitle-text">{{ subtitle }}</p>
            </div>

            <div class="footer-container">
                <!-- 日期 + 分类 -->
                <div class="info-row">
                    <span class="created-date">
                        <v-icon class="created-date-icon" icon="mdi-alarm" size="small" start></v-icon>
                        <span class="created-date-text">{{ createdDate }}</span>
                    </span>
                    <span class="second-class">
                        <v-icon class="second-class-icon" icon="mdi-hexagon-multiple-outline" size="small"
                                start></v-icon>
                         <span class="second-class-text">{{ secondClassification }}</span>
                    </span>
                </div>

                <!-- 分割线 -->
                <div class="divider"></div>

                <!-- tags -->
                <div class="tags">
                    <template v-for="(tag, index) in tags" :key="index">
                        <span class="tag">
                            <v-icon class="tag-icon" icon="mdi-tag-outline"></v-icon>
                            <span class="tag-text">{{ tag }}</span>
                        </span>
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang='ts'>

    defineOptions({
        name: 'Card',
        inheritAttrs: false
    })

    // title、subtitle、bgImage、createdDate、secondClassification、tags
    defineProps<{
        title: string
        subtitle: string
        bgImage: string
        createdDate: string
        secondClassification: string
        tags: string[]
    }>()

</script>


<style scoped lang='scss'>
    .card-container {
        position: relative;
        width: 100%;
        max-width: 360px;
        height: 250px;
        margin: 0 auto;
        border-radius: 5px;
        overflow: hidden;
        background-image: url("src/assets/3.jpg");
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: stretch;
        justify-content: flex-start;
        transition: transform 0.3s ease;

        &:hover {
            transform: scale(1.03);
            z-index: 3;
        }

        .overlay {
            background-image: linear-gradient(to bottom,
                rgba(0, 0, 0, 0.25) 0%,
                rgba(0, 0, 0, 0.35) 10%,
                rgba(0, 0, 0, 0.45) 20%,
                rgba(0, 0, 0, 0.55) 30%,
                rgba(0, 0, 0, 0.65) 40%,
                rgba(0, 0, 0, 0.65) 50%,
                rgba(0, 0, 0, 0.65) 60%,
                rgba(0, 0, 0, 0.55) 70%,
                rgba(0, 0, 0, 0.45) 80%,
                rgba(0, 0, 0, 0.35) 90%,
                rgba(0, 0, 0, 0.25) 100%,
            );
            width: 100%;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            color: #ffffff;
            height: 100%;
        }

        .text-container {
            margin: 40px 10px 20px 10px;

            .title-text {
                margin: 0 0 10px 10px;
                font-size: 18px;
                font-weight: bold;
                color: white;
            }

            .subtitle-text {
                margin: 20px 0 10px 10px;
                font-size: 14px;
                color: #bbbbbb;
            }
        }

        .footer-container {
            margin: auto 15px 5px 15px;

            // 日期 + 分类：同一行两端对齐
            .info-row {
                display: flex;
                justify-content: space-between;
                font-size: 12px;

                .created-date {
                    color: #bbbbbb;
                    display: flex;
                    align-items: center;

                    .created-date-text {
                        font-size: 14px;
                    }

                    .created-date-icon {

                    }
                }

                .second-class {
                    color: #bbbbbb;
                    display: flex;
                    align-items: center;

                    .second-class-text {
                        font-size: 14px;
                    }

                    .second-class-icon {

                    }
                }

            }

            // 分割线
            .divider {
                height: 1.5px;
                background-color: rgba(255, 255, 255, 0.5);
                margin: 5px 0;
            }

            // 标签区域
            .tags {
                margin: 10px 0 0 0;
                display: flex;
                gap: 8px;

                .tag {
                    background: rgba(255, 255, 255, 0.2);
                    padding: 2px 5px;
                    border-radius: 4px;
                    font-size: 12px;

                    .tag-icon {
                        font-size: 14px;
                    }

                    .tag-text {
                    }
                }
            }
        }
    }
</style>
