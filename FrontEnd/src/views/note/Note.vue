<template>
    <div class="content-container">
        <div class="article-list">
            <template v-for="item in noteStore.noteList" :key="item.noteListId">
                <Card
                    :title="item.title"
                    :bgImage="item.coverImg"
                    :createdDate="item.createdTime"
                    :category="item.category"
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
                <!-- 标签、分类展示区域 -->
                <div class="tags-category-container">
                    <div class="tags-container">
                    <span class="tag" v-for="(tag, index) in currentDetail?.tagsName" :key="index">
                        {{ tag }}
                    </span>
                    </div>
                    <div class="category-container">
                        <span class="category">
                            <v-icon class="category-icon" icon="mdi-bookmark-multiple"></v-icon>
                            <span class="category-text">{{ currentDetail?.category }}</span>
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
                <!-- 文章摘要展示区域 -->
                <div class="brief-container">
                    <span class="brief">{{ currentDetail?.brief }}</span>
                </div>

                <!-- 按钮展示区域-->
                <div class="action-container">
                    <div class="read-more">
                        <v-btn class="read-more-btn" variant="flat"
                               @click="jumpToNoteDetail(currentDetail.noteListId)">
                            <span class="read-more-text">阅读</span>
                        </v-btn>
                    </div>
                    <div class="exit">
                        <v-btn class="exit-btn" variant="flat" @click="closeDialog">
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

    const jumpToNoteDetail = (noteListId: number) => {
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
            padding: 120px 20px 30px 20px;
            justify-items: center;
        }
    }

    .card-dialog {
        position: fixed;
        inset: 0;
        background-color: rgba(255, 255, 255, 0.3);
        display: flex;
        justify-content: center;
        align-items: flex-start;
        z-index: 2000;
        overflow-y: auto;
        padding: 40px 20px;

        .dialog-background {
            width: 50%;
            height: 42em;
            position: fixed;
            top: 6em;
            background-color: rgba(255, 255, 255);
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
                background: rgba(255, 255, 255, 0.85);
                border-radius: 10px;
                padding: 20px;
                position: relative;
                top: -7.5em;
                left: 4.5em;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);

                .tags-category-container {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 12px;

                    .tags-container {
                        display: flex;
                        flex-wrap: wrap;
                        gap: 6px;

                        .tag {
                            background-color: rgb(0, 100, 100);
                            color: white;
                            padding: 6px 10px;
                            border-radius: 10px;
                            font-size: 0.65rem;
                            font-weight: 800;
                        }
                    }

                    .category-container {

                        .category {
                            background-color: white;
                            padding: 6px 10px;
                            border-radius: 10px;
                            display: flex;
                            align-items: center;
                            gap: 4px;

                            .category-icon {
                                font-size: 0.65rem;
                                color: rgb(0, 100, 100);
                            }

                            .category-text {
                                font-size: 0.65rem;
                                font-weight: 800;
                                color: rgb(0, 100, 100);
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
                        color: rgba(0, 40, 40, 0.75);
                        font-size: 0.9rem;
                    }

                    .created-date-text {
                        color: rgba(0, 40, 40, 0.75);
                        font-size: 0.9rem;
                    }
                }

                .modified-date {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .modified-date-icon {
                        color: rgba(0, 40, 40, 0.75);
                        font-size: 0.9rem;
                    }

                    .modified-date-text {
                        color: rgba(0, 40, 40, 0.75);
                        font-size: 0.9rem;
                    }
                }

                .viewed {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .viewed-icon {
                        color: rgba(0, 40, 40, 0.75);
                        font-size: 0.9rem;
                    }

                    .viewed-text {
                        color: rgba(0, 40, 40, 0.75);
                        font-size: 0.9rem;
                    }
                }

                .liked {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .liked-icon {
                        color: rgba(0, 40, 40, 0.75);
                        font-size: 0.9rem;
                    }

                    .liked-text {
                        color:rgba(0, 40, 40, 0.75);
                        font-size: 14px;
                    }
                }

                .disgusted {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .disgusted-icon {
                        color: rgba(0, 40, 40, 0.75);
                        font-size: 0.9rem;
                    }

                    .disgusted-text {
                        color: rgba(0, 40, 40, 0.75);
                        font-size: 0.9rem;
                    }
                }
            }

            .title-container {
                margin: 25px 0 0 0;

                .title {
                    font-size: 1.75rem;
                    font-weight: 900;
                    color: rgba(0, 100, 100);;
                }
            }

            .brief-container {
                margin: 25px 0 0 0;

                .brief {
                    font-size: 1rem;
                    color: rgba(0, 40, 40, 0.9);
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
                        background-color: rgba(0, 100, 100);

                        .read-more-text {
                            color: white;
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
                        background-color:  rgba(0, 100, 100);

                        .exit-text {
                            color: white;
                            font-size: 0.85rem;
                        }
                    }
                }
            }
        }
    }
</style>