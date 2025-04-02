<template>
    <div class="content-container">
        <div class="article-list">
            <template v-for="item in noteStore.noteList" :key="item.noteListId">
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
                    backgroundImage: `linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.2)), url(${encodeURI(currentDetail?.coverImg)})`,
                    filter: 'blur(1px)'
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
                            <v-icon class="classification-icon" icon="mdi-bookmark-multiple"></v-icon>
                            <span class="classification-text">{{ currentDetail?.secondClassification }}</span>
                        </span>
                    </div>
                </div>

                <!-- 创建时间、更新时间等展示区域 -->
                <div class="article-info-container">
                    <span class="created-date">
                        <v-icon class="created-date-icon" icon="mdi-calendar-sync-outline"></v-icon>
                        <span class="created-date-text">{{ currentDetail?.createdTime }}</span>
                    </span>
                    <span class="modified-date">
                        <v-icon class="modified-date-icon" icon="mdi-calendar-sync-outline"></v-icon>
                        <span class="modified-date-text">{{ currentDetail?.modifiedTime }}</span>
                    </span>

                    <span class="viewed">
                        <v-icon class="viewed-icon" icon="mdi-eye-outline"></v-icon>
                        <span class="viewed-text">{{ currentDetail?.viewedCount }}</span>
                    </span>

                    <span class="liked">
                        <v-icon class="liked-icon" icon="mdi-heart-outline"></v-icon>
                        <span class="liked-text">{{ currentDetail?.likedCount }}</span>
                    </span>

                    <span class="disgusted">
                        <v-icon class="disgusted-icon" icon="mdi-heart-off-outline"></v-icon>
                        <span class="disgusted-text">{{ currentDetail?.disgustedCount }}</span>
                    </span>

                </div>

                <!-- 文章标题展示区域 -->
                <div class="title-container">
                    <span class="title">{{ currentDetail?.title }}</span>
                </div>
                <!-- 文章副标题展示区域 -->
                <div class="subtitle-container">
                    <span class="subtitle">{{ currentDetail?.subtitle }}</span>
                </div>
                <!-- 文章摘要展示区域 -->
                <div class="brief-container">
                    <span class="brief">{{ currentDetail?.brief }}</span>
                </div>

                <!-- 按钮展示区域-->
                <div class="action-container">
                    <div class="read-more">
                        <v-btn class="read-more-btn" variant="outlined"
                               @click="jumpToNoteDetail(currentDetail.noteListId)">
                            <span class="read-more-text">阅读</span>
                        </v-btn>
                    </div>
                    <div class="exit">
                        <v-btn class="exit-btn" variant="outlined" @click="closeDialog">
                            <span class="exit-text">离开</span>
                        </v-btn>
                    </div>
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

    const jumpToNoteDetail =  (noteListId: number) => {
         $router.push({
            name: 'noteDetail',
            params: {
                id: noteListId
            }
        })
    }

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
            width: 50%;
            height: 40em;
            position: fixed;
            top: 6em;
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 10px 10px 10px 10px;

            .dialog-cover-container {

                .dialog-cover {
                    height: 400px;
                    background-size: cover;
                    background-position: center;
                    border-radius: 12px 12px 0 0;
                }
            }

            .dialog-content-container {
                width: 80%;
                background: rgba(255, 255, 255, 0.75);
                border-radius: 10px;
                padding: 20px;
                position: relative;
                top: -8em;
                left: 5.6em;
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
                            background-color: #113c46;
                            color: white;
                            padding: 6px 10px;
                            border-radius: 10px;
                            font-size: 0.7rem;
                        }
                    }

                    .classification-container {

                        .classification {
                            background-color: white;
                            padding: 6px 10px;
                            border-radius: 10px;
                            display: flex;
                            align-items: center;
                            gap: 4px;

                            .classification-icon {
                                font-size: 0.7rem;
                                color: #113c46;
                            }

                            .classification-text {
                                font-size: 0.7rem;
                                color: #113c46;
                            }
                        }
                    }
                }
            }

            .article-info-container {
                display: flex;
                flex-wrap: wrap;
                gap: 30px;
                margin: 30px 0 20px 0;

                .created-date {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .created-date-icon {
                        color: #515c7a;
                        font-size:0.9rem;
                    }

                    .created-date-text {
                        color: #515c7a;
                        font-size: 0.9rem;
                    }
                }

                .modified-date {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .modified-date-icon {
                        color: #515c7a;
                        font-size: 0.9rem;
                    }

                    .modified-date-text {
                        color: #515c7a;
                        font-size:0.9rem;
                    }
                }

                .viewed {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .viewed-icon {
                        color: #515c7a;
                        font-size: 0.9rem;
                    }

                    .viewed-text {
                        color: #515c7a;
                        font-size: 0.9rem;
                    }
                }

                .liked {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .liked-icon {
                        color: #515c7a;
                        font-size: 0.9rem;
                    }

                    .liked-text {
                        color: #515c7a;
                        font-size: 14px;
                    }
                }

                .disgusted {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .disgusted-icon {
                        color: #515c7a;
                        font-size: 0.9rem;
                    }

                    .disgusted-text {
                        color: #515c7a;
                        font-size: 0.9rem;
                    }
                }
            }

            .title-container {
                margin: 25px 0 0 0;

                .title {
                    font-size: 1.75rem;
                    font-weight: 900;
                }
            }

            .subtitle-container {
                margin: 25px 0 0 0;

                .subtitle {
                    font-size: 1.25rem;
                    font-weight: 600;
                    color: #666;
                    margin-bottom: 16px;
                }
            }

            .brief-container {
                margin: 25px 0 0 0;

                .brief {
                    font-size: 1rem;
                    color: #888888;
                    line-height: 1.6;
                }
            }

            .action-container {
                display: flex;
                flex-direction: row;
                justify-content: flex-end;
                gap: 35px;
                margin: 20px 30px 10px 0;

                .read-more {
                    .read-more-btn {
                        width: 1rem;
                        height: 2rem;
                        display: flex;
                        align-items: center;
                        justify-content: center;

                        .read-more-text {
                            color: #515c7a;
                            font-size: 0.85rem;
                        }
                    }
                }

                .exit {
                    .exit-btn {
                        width: 1rem;
                        height: 2rem;
                        display: flex;
                        align-items: center;
                        justify-content: center;

                        .exit-text {
                            color: #515c7a;
                             font-size: 0.85rem;
                        }
                    }
                }
            }
        }
    }
</style>