<template>

    <div class="header-container">
        <div class="header" :class="{'change-bgcolor':isScrollOverViewport}">
            <div class="title-big">
                <HeaderTitle></HeaderTitle>
            </div>
            <div class="nav-big">
                <HeaderNav></HeaderNav>
            </div>
            <div class="widget-big">
                <HeaderWidget></HeaderWidget>
            </div>
        </div>
    </div>

    <div class="coverImage" ref="coverImageRef"
         :style="{ backgroundImage: `linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.2)), url(${noteContentItem.coverImg})`,
         filter: 'blur(1px)'}"></div>

    <div class="article-title-container">
        <span class="article-title">{{ noteContentItem.title }}</span>
    </div>

    <div class="article-subtitle-container">
        <span class="article-subtitle">{{ noteContentItem.subtitle }}</span>
    </div>

    <div class="article-content-container">
        <div class="article-background">

            <!-- 标签、二级分类区域 -->
            <div class="tags-classification-container">
                <div class="tags-container">
                    <span class="tag" v-for="(tag, index) in noteContentItem.tagsName" :key="index">
                        {{ tag }}
                    </span>
                </div>
                <div class="classification-container">
                    <span class="classification">
                        <v-icon class="classification-icon" icon="mdi-bookmark-multiple"></v-icon>
                        <span class="first-classification-text">{{ noteContentItem.firstClassification }}</span>
                        <span> / </span>
                        <span class="second-classification-text">{{ noteContentItem.secondClassification }}</span>
                    </span>
                </div>
            </div>

            <!-- 创建时间、更新时间等区域 -->
            <div class="article-info-container">
                <span class="created-date">
                    <v-icon class="created-date-icon" icon="mdi-calendar-sync-outline"></v-icon>
                    <span class="created-date-text">{{ noteContentItem.createdTime }}</span>
                </span>

                <span class="modified-date">
                    <v-icon class="modified-date-icon" icon="mdi-calendar-sync-outline"></v-icon>
                    <span class="modified-date-text">{{ noteContentItem.modifiedTime }}</span>
                </span>

                <span class="viewed">
                    <v-icon class="viewed-icon" icon="mdi-eye-outline"></v-icon>
                    <span class="viewed-text">{{ noteContentItem.viewedCount }}</span>
                </span>

                <span class="liked">
                    <v-icon class="liked-icon" icon="mdi-heart-outline"></v-icon>
                    <span class="liked-text">{{ noteContentItem.likedCount }}</span>
                </span>
                <span class="disgusted">
                    <v-icon class="disgusted-icon" icon="mdi-heart-off-outline"></v-icon>
                    <span class="disgusted-text">{{ noteContentItem.disgustedCount }}</span>
                </span>
            </div>

            <div class="divider1"></div>

            <!-- 文章正文区域 -->
            <div class="article-body-container">
                <span class="article-body">
                    {{ noteContentItem.content }}
                </span>
            </div>
            <div class="divider2"></div>
            <div class="article-footer-container">
                <div class="author-container">
                    <span class="author">
                        <v-icon class="author-icon" icon="mdi-account-outline"></v-icon>
                        <span class="author-text">文章作者：WangBo</span>
                    </span>
                </div>
                <div class="link-container">
                    <span class="link">
                        <v-icon class="link-icon" icon="mdi-link"></v-icon>
                        <span class="link-text">文章链接：https://127.0.0.1:8001/article/2</span>
                    </span>
                </div>
                <div class="copy-right-container">
                    <span class="copy-right">
                        <v-icon class="copy-right-icon" icon="mdi-copyright"></v-icon>
                        <span class="copy-right-text">版权声明：本博客所有文章除特別声明外，均采用 CC BY 4.0 许可协议。转载请注明来源 WangBo</span>
                    </span>
                </div>
            </div>

            <div class="outlink-container">

            </div>
        </div>
    </div>

</template>

<script setup lang='ts'>
    import {useRoute, useRouter} from "vue-router";
    import {onMounted, onUnmounted, reactive, ref} from "vue";
    import useNoteStore from "@/store/note.ts";
    import axios_server from "@/utils/axios_server.ts";
    import type {NoteContentItem} from "@/store/types/note.ts";
    import HeaderNav from "@/components/Header/HeaderNav.vue";
    import HeaderTitle from "@/components/Header/HeaderTitle.vue";
    import HeaderWidget from "@/components/Header/HeaderWidget.vue";

    defineOptions({
        name: 'Detail',
        inheritAttrs: false
    })

    const route = useRoute()
    const $router = useRouter()
    const noteStore = useNoteStore()
    const noteListId = Number(route.params.id)
    const noteContentItem = reactive<NoteContentItem>({
        "noteListId": 0,
        "title": '',
        "subtitle": '',
        "brief": '',
        "coverImg": '',
        "isShow": true,
        "isPinned": false,
        "isRecommended": false,
        "viewedCount": 0,
        "likedCount": 0,
        "disgustedCount": 0,
        "encouragedCount": 0,
        "createdTime": '',
        "modifiedTime": '',
        "tagsName": [],
        "firstClassification": '',
        "secondClassification": '',
        "content": ''
    })

    // 获取class="coverImage"的DOM
    let coverImageRef = ref<HTMLElement | null>(null)
    // 是否滚动过封面区域
    let isScrollOverViewport = ref(false)
    // 滚动监听函数
    const handleScroll = () => {
        if (coverImageRef.value) {
            let rect = coverImageRef.value.getBoundingClientRect()
            isScrollOverViewport.value = rect.bottom <= 55
        }
    }

    onMounted(async () => {
        // 页面加载时，从noteStore中获取文章list
        const result = noteStore.noteList.find(note => note.noteListId === noteListId)
        // 页面加载时，从后端获取文章content
        const content = await axios_server.get('getNote/', {
            params: {
                noteListId
            }
        })
        Object.assign(noteContentItem, result)
        noteContentItem.content = content.data.content

        // 页面挂载时监听handleScroll
        window.addEventListener('scroll', handleScroll)
        const rect = coverImageRef.value!.getBoundingClientRect()
        isScrollOverViewport.value = rect.bottom <= 55
    })

    onUnmounted(() => {
        // 页面卸载时移除监听
        window.removeEventListener('scroll', handleScroll)
    })

    const goBack = () => {
        $router.back()
    }

</script>

<style scoped lang='scss'>
    .header-container {
        padding: 0;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 5vh;
        z-index: 1000;

        .header {
            display: flex;
            justify-content: center;
            align-items: stretch;
            height: 100%;
            width: 100%;
            background-color: rgba(100, 100, 100, 0.5);

            .title-big {
                width: 35%;
                height: 100%;
                padding-right: 30px;
            }

            .nav-big {
                width: 35%;
                height: 100%;
            }

            .widget-big {
                width: 30%;
                height: 100%;
            }
        }

        .change-bgcolor {
            background-color: #113c46;
        }
    }

    .coverImage {
        width: 100%;
        height: 50vh;
        background-size: cover;
        background-position: top center;
        background-repeat: no-repeat;
        background-position-x: 10%;
        background-position-y: 50%;
        filter: brightness(0.5);
    }

    .article-title-container {

        .article-title {
            padding: 10px 300px 10px 10px;
            border-radius: 2px 10px 2px 2px;
            position: relative;
            top: -350px;
            left: 500px;
            font-size: 40px;
            background-color: rgba(35, 100, 100, 0.5);
            color: #eeeeee;
        }
    }

    .article-subtitle-container {

        .article-subtitle {
            padding: 10px 10px 10px 300px;
            border-radius: 2px 2px 2px 10px;
            position: relative;
            top: -317px;
            left: 700px;
            font-size: 25px;
            background-color: rgba(238, 238, 238, 0.5);
            color: #163d3d;
        }
    }


    .article-content-container {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        z-index: 900;

        .article-background {
            padding: 50px 80px 20px 80px;
            width: 70%;
            position: relative;
            top: -160px;
            //background-color: rgba(255, 255, 255, 0.99);
            border-radius: 10px 10px 10px 10px;
            background-image: linear-gradient(to top,
                rgba(255, 255, 255, 0.6) 90%,
                rgba(255, 255, 255, 0.58) 91%,
                rgba(255, 255, 255, 0.56) 92%,
                rgba(255, 255, 255, 0.54) 93%,
                rgba(255, 255, 255, 0.52) 94%,
                rgba(255, 255, 255, 0.5) 95%,
                rgba(255, 255, 255, 0.48) 96%,
                rgba(255, 255, 255, 0.46) 97%,
                rgba(255, 255, 255, 0.44) 98%,
                rgba(255, 255, 255, 0.42) 99%,
                rgba(255, 255, 255, 0.4) 100%
            );
            box-shadow: 0 6px 6px rgba(0, 0, 0, 0.1);

            .tags-classification-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 12px;

                .tags-container {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;

                    .tag {
                        background-color: #113c46;
                        color: white;
                        padding: 6px 10px;
                        border-radius: 5px;
                        font-size: 16px;
                    }
                }

                .classification-container {

                    .classification {
                        padding: 6px 10px;
                        border-radius: 10px;
                        background-color: white;
                        display: flex;
                        align-items: center;
                        gap: 5px;

                        .classification-icon {
                            font-size: 16px;
                            color: #113c46;
                        }

                        .first-classification-text {
                            font-size: 16px;
                            font-weight: 700;
                            color: #113c46;
                        }

                        .second-classification-text {
                            font-size: 16px;
                            font-weight: 400;
                            color: #113c46;
                        }
                    }
                }
            }

            .divider1 {
                width: 100%;
                height: 2px;
                background-color: #515c7a;;
                margin: 10px 0 40px 0;
            }

            .article-info-container {
                display: flex;
                flex-wrap: wrap;
                gap: 30px;
                margin: 30px 0 10px 0;

                .created-date {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .created-date-icon {
                        color: #515c7a;
                        font-size: 18px;
                    }

                    .created-date-text {
                        color: #515c7a;
                        font-size: 18px;
                    }
                }

                .modified-date {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .modified-date-icon {
                        color: #515c7a;
                        font-size: 18px;
                    }

                    .modified-date-text {
                        color: #515c7a;
                        font-size: 18px;
                    }
                }

                .viewed {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .viewed-icon {
                        color: #515c7a;
                        font-size: 18px;
                    }

                    .viewed-text {
                        color: #515c7a;
                        font-size: 18px;
                    }
                }

                .liked {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .liked-icon {
                        color: #515c7a;
                        font-size: 18px;
                    }

                    .liked-text {
                        color: #515c7a;
                        font-size: 18px;
                    }
                }

                .disgusted {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .disgusted-icon {
                        color: #515c7a;
                        font-size: 18px;
                    }

                    .disgusted-text {
                        color: #515c7a;
                        font-size: 18px;
                    }
                }
            }

            .article-body-container {
                .article-body {
                    font-size: 20px;
                }
            }

            .divider2 {
                width: 100%;
                height: 2px;
                background-color: #515c7a;;
                margin: 20px 0 20px 0;
            }

            .article-footer-container {
                padding: 15px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(150, 150, 150, 0.3);
                display: flex;
                flex-wrap: wrap;
                gap: 15px;
                margin: 30px 0 20px 0;
                background-color: rgba(250, 250, 250, 0.2);
                border: 1px solid rgba(150, 150, 150, 0.3);

                .author-container {
                    .author {
                        display: flex;
                        align-items: center;
                        gap: 1px;

                        .author-icon {
                            color: #515c7a;
                            font-size: 20px;
                        }

                        .author-text {
                            color: black;
                            font-size: 16px;
                            font-weight: 800;
                        }
                    }
                }

                .link-container {
                    .link {
                        display: flex;
                        align-items: center;
                        gap: 2px;

                        .link-icon {
                            color: #515c7a;
                            font-size: 20px;
                        }

                        .link-text {
                            color: black;
                            font-size: 16px;
                            font-weight: 800;
                        }
                    }
                }

                .copy-right-container {
                    .copy-right {
                        display: flex;
                        align-items: center;
                        gap: 4px;

                        .copy-right-icon {
                            color: #515c7a;
                            font-size: 20px;
                        }

                        .copy-right-text {
                            color: black;
                            font-size: 16px;
                            font-weight: 800;
                        }
                    }
                }
            }
        }
    }


    .change-bgcolor {
        background-color: #113c46;
    }
</style>