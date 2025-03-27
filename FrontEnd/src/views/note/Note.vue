<template>
    <div class="content-container">
        <div class="article-list">
            <template v-for="(item, index) in noteStore.noteList" :key="item.noteListId">
                <Card
                    :title="item.title"
                    :subtitle="item.subtitle"
                    :bgImage="item.coverImg"
                    :createdDate="item.createdTime"
                    :secondClassification="item.secondClassification"
                    :tags="item.tagsName"
                    @click="() => openDialog(item.noteListId)"
                ></Card>
            </template>
        </div>
    </div>

    <!-- dialog -->
    <div class="card-dialog" v-if="showDialog" @click.self="closeDialog">
        <div class="dialog-background">
            <!-- 顶部封面图 -->
            <div class="dialog-cover-container">
                <div class="dialog-cover" :style="{
                    backgroundImage: `linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.2)), url(${currentDetail?.coverImg})`,
                    filter: 'blur(3px)'
                }"></div>
            </div>
            <!-- 内容展示区域 -->
            <div class="dialog-content-container">
                <!-- 标签、二级分类展示区域 -->
                <div class="tags-classification-container">
                    <div class="tags-container">
                    <span class="tag" v-for="(tag, index) in currentDetail?.tagsName" :key="index">
                        {{ tag }}
                    </span>
                    </div>
                    <div class="classification-container">
                    <span class="classification">
                        {{ currentDetail?.secondClassification }}
                    </span>
                    </div>
                </div>
                <!-- 创建时间、更新时间等信息展示 -->
                <div class="article-info-container">
                    <span>{{ currentDetail?.createdTime }}</span>
                    <span>{{ currentDetail?.modifiedTime }}</span>
                    <span>{{ currentDetail?.viewedCount }}</span>
                    <span>{{ currentDetail?.likeCount }}</span>
                    <span>{{ currentDetail?.disgustedCount }}</span>
                    <span v-if="currentDetail?.isPinned">置顶</span>
                    <span v-if="currentDetail?.isRecommended">推荐</span>
                </div>
                <!-- 文章标题 -->
                <div class="title-container">
                    <span class="title">{{ currentDetail?.title }}</span>
                </div>
                <!-- 文章副标题 -->
                <div class="subtitle-container">
                    <span class="subtitle">{{ currentDetail?.subtitle }}</span>
                </div>
                <!-- 文章摘要 -->
                <div class="brief-container">
                    <span class="brief">{{ currentDetail?.brief }}</span>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup lang='ts'>
    import useNoteStore from "@/store/note.ts";
    import {useRouter} from "vue-router";
    import {onMounted, onUnmounted, ref} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";
    import Card from "@/components/Card.vue";

    defineOptions({
        name: 'Note',
        inheritAttrs: false
    })

    const noteStore = useNoteStore()
    const $router = useRouter()
    let appearanceStore = useAppearanceStore()

    // dialog状态控制
    const showDialog = ref(false)
    const currentDetail = ref<any>(null)

    const openDialog = (noteListId: number) => {
        const found = noteStore.noteList.find(item => item.noteListId === noteListId)
        if (found) {
            currentDetail.value = found
            showDialog.value = true
        }
    }

    const closeDialog = () => {
        showDialog.value = false
        currentDetail.value = null
    }

    // const jumpTo = (noteListId: number) => {
    //     $router.push({
    //         name: 'noteDetail',
    //         params: {
    //             id: noteListId
    //         }
    //     })
    // }

    onMounted(() => {
        appearanceStore.isShowHomeCover = false
        appearanceStore.isScrollOverViewport = true
    })

    onUnmounted(() => {
        appearanceStore.isShowHomeCover = true
    })

</script>

<style scoped lang="scss">
    .content-container {
        position: relative;
        width: 100%;
        height: 100%;

        .article-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            column-gap: 34px;
            row-gap: 40px;
            padding: 80px 20px 30px 20px;
            justify-items: center;
        }
    }

    .card-dialog {
        position: fixed;
        inset: 0;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: flex-start;
        z-index: 2000;
        overflow-y: auto;
        padding: 40px 20px;

        .dialog-background {
            width: 60%;
            height: 80vh;
            position: fixed;
            top: 100px;
            background-color: white;
            border-radius: 12px 12px 12px 12px;
            color: red;

            .dialog-cover-container {

                .dialog-cover {
                    height: 300px;
                    background-size: cover;
                    background-position: center;
                    border-radius: 12px 12px 0 0;
                }
            }

            .dialog-content-container {
                width: 95%;
                background: #ffffff;
                border-radius: 10px;
                padding: 24px;
                position: relative;
                top: -20px;
                left: 30px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);

                .tags-classification-container {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 12px;

                    .tags-container {
                        display: flex;
                        flex-wrap: wrap;
                        gap: 6px;

                        .tag {
                            background-color: #17687a;
                            color: white;
                            padding: 4px 8px;
                            border-radius: 10px;
                            font-size: 12px;
                        }
                    }

                    .classification-container {

                        .classification {
                            font-size: 14px;
                            color: black;
                            font-weight: 500;

                        }
                    }
                }
            }

            .article-info-container {
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
                font-size: 14px;
                color: #888888;
                margin-bottom: 16px;
            }

            .title-container {
                .title {
                    font-size: 22px;
                    font-weight: bold;
                    margin-bottom: 8px;
                }
            }

            .subtitle-container {
                .subtitle {
                    font-size: 16px;
                    color: #666;
                    margin-bottom: 16px;
                }
            }

            .brief-container {
                .brief {
                    font-size: 14px;
                    color: #444;
                    line-height: 1.6;
                }
            }
        }


    }


</style>