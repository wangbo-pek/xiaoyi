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
         :style="{ backgroundImage: `linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.2)), url(${noteStore.currentNote.coverImg})`,
         filter: 'blur(1px)'}"></div>

    <div class="article-title-container">
        <span class="article-title">{{ noteStore.currentNote.title }}</span>
    </div>

    <div class="article-content-container">
        <div class="article-background">

            <!-- 标签、二级分类区域 -->
            <div class="tags-category-container">
                <div class="tags-container">
                    <span class="tag" v-for="(tag, index) in noteStore.currentNote.tagsName" :key="index">
                        {{ tag }}
                    </span>
                </div>
                <div class="category-container">
                    <span class="category">
                        <v-icon class="category-icon" icon="mdi-bookmark-multiple"></v-icon>
                        <span class="category-text">{{ noteStore.currentNote.category }}</span>
                    </span>
                </div>
            </div>

            <!-- 创建时间、更新时间等区域 -->
            <div class="article-info-container">
                <span class="created-date">
                    <v-icon class="created-date-icon" icon="mdi-calendar-sync-outline"></v-icon>
                    <span class="created-date-text">{{ noteStore.currentNote.createdTime }}</span>
                </span>

                <span class="modified-date">
                    <v-icon class="modified-date-icon" icon="mdi-calendar-sync-outline"></v-icon>
                    <span class="modified-date-text">{{ noteStore.currentNote.modifiedTime }}</span>
                </span>

                <span class="viewed">
                    <v-icon class="viewed-icon" icon="mdi-eye-outline"></v-icon>
                    <span class="viewed-text">{{ noteStore.currentNote.viewedCount }}</span>
                </span>

                <span class="liked">
                    <v-icon class="liked-icon" icon="mdi-heart-outline"></v-icon>
                    <span class="liked-text">{{ noteStore.currentNote.likedCount }}</span>
                </span>
                <span class="disgusted">
                    <v-icon class="disgusted-icon" icon="mdi-heart-off-outline"></v-icon>
                    <span class="disgusted-text">{{ noteStore.currentNote.disgustedCount }}</span>
                </span>
            </div>

            <div class="divider1"></div>

            <!-- 文章正文区域 -->
            <div class="article-body-container">
                <div class="article-body markdown-content" v-html="noteStore.currentNote.renderedMarkdown"></div>
            </div>

            <!-- toc内容 -->
            <div class="toc markdown-content">
                <div class="toc-title">
                    <v-icon class="toc-title-icon" icon="mdi-table-of-contents"></v-icon>
                    <span class="toc-title-text">目录</span>
                </div>
                <div v-html="toc"></div>
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

            <div class="share-container">
                <div class="tags">
                    <span class="tag" v-for="(tag, index) in noteStore.currentNote.tagsName" :key="index">{{
                            tag
                        }}</span>
                </div>
                <div class="share-icon">
                    <v-img class="shaoshupai-icon" :src="shaoshupai.svgIconUrl"
                           @click="jumpToSocialMedia(shaoshupai.name)"></v-img>
                    <v-img class="github-icon" :src="github.svgIconUrl" @click="jumpToSocialMedia(github.name)"></v-img>
                    <v-img class="weibo-icon" :src="weibo.svgIconUrl" @click="jumpToSocialMedia(weibo.name)"></v-img>
                    <v-img class="douban-icon" :src="douban.svgIconUrl" @click="jumpToSocialMedia(douban.name)"></v-img>
                    <v-img class="zhihu-icon" :src="zhihu.svgIconUrl" @click="jumpToSocialMedia(zhihu.name)"></v-img>
                    <v-img class="twitter-icon" :src="twitter.svgIconUrl"
                           @click="jumpToSocialMedia(twitter.name)"></v-img>
                    <v-img class="facebook-icon" :src="facebook.svgIconUrl"
                           @click="jumpToSocialMedia(facebook.name)"></v-img>
                </div>
            </div>

            <div class="coffee-container" @click="showCoffeeDialog = true">
                <span class="coffee-text">{{ coffeeMe.title }}</span>
                <v-img class="coffee-icon" :src="coffeeMe.svgIconUrl"></v-img>
            </div>
        </div>
    </div>

    <div class="recommend-note-container">
    </div>

    <!-- coffee me -->
    <v-dialog v-model="showCoffeeDialog" width="800">
        <v-card class="qr-card" color="#1e1e1e">
            <v-card-title class="text-center text-white">感谢您的支持!</v-card-title>
            <v-card-text class="text-center">
                <div style="display: flex; justify-content: center; gap: 20px;">
                    <v-img
                        :src="coffeeMe.coffeeMeAlipayInfo"
                        aspect-ratio="1"
                        max-width="40%"
                    />
                    <v-img
                        :src="coffeeMe.coffeeMeWechatInfo"
                        aspect-ratio="1"
                        max-width="40%"
                    />
                </div>
            </v-card-text>
            <v-card-actions class="justify-center">
                <v-btn color="rgb(242, 204, 15)" @click="showCoffeeDialog = false">关闭</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

</template>

<script setup lang='ts'>
    import {useRoute} from "vue-router";
    import {onMounted, onUnmounted, ref, watchEffect} from "vue";
    import useNoteStore from "@/store/note.ts";
    import {useRouter} from "vue-router";
    import axios_server from "@/utils/axios_server.ts";
    import HeaderNav from "@/components/header/HeaderNav.vue";
    import HeaderTitle from "@/components/header/HeaderTitle.vue";
    import HeaderWidget from "@/components/header/HeaderWidget.vue";
    import MarkdownIt from 'markdown-it';
    import hljs from 'highlight.js'
    import 'highlight.js/styles/github.css'
    import {twitter, facebook, github, douban, weibo, zhihu, shaoshupai} from '@/data/socialMedia.ts'
    import {coffeeMe, mailMe, rssMe} from "@/data/personalDetail.ts";

    defineOptions({
        name: 'NoteDetail',
        inheritAttrs: false
    })

    const md = new MarkdownIt({
        html: true
    })
    const route = useRoute()
    const noteStore = useNoteStore()
    const noteListId = Number(route.params.id)
    const $router = useRouter()

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

    // 前端展示table of contents的内容
    const toc = ref('');

    const handleTableOfContents = () => {
        const regex = /<h1>(.*?)<\/h1>/g;
        let match;
        let tocHtml = '<ul>';
        let counter = 1;
        let updatedMarkdown = noteStore.currentNote.renderedMarkdown;

        while ((match = regex.exec(noteStore.currentNote.renderedMarkdown)) !== null) {
            const headingText = match[1];
            const id = `heading-${counter}`;

            // 将原始的 <h1>标签 替换为带 id 的 <h1 id="heading-1">
            const originalHeading = match[0]; // <h1>标题</h1>
            const updatedHeading = `<h1 id="${id}">${headingText}</h1>`;
            updatedMarkdown = updatedMarkdown.replace(originalHeading, updatedHeading);

            // 构建 TOC 目录项
            tocHtml += `<li><a href="#${id}">${headingText}</a></li>`;
            counter++;
        }

        tocHtml += '</ul>';
        // 更新 markdown 和 TOC 内容
        noteStore.currentNote.renderedMarkdown = updatedMarkdown;
        toc.value = tocHtml;
    }

    const jumpToSocialMedia = (name: string) => {
        const urlMap: Record<string, string> = {
            weibo: weibo.linkUrl,
            douban: douban.linkUrl,
            zhihu: zhihu.linkUrl,
            twitter: twitter.linkUrl,
            facebook: facebook.linkUrl,
            github: github.linkUrl,
        }

        const url = urlMap[name]
        if (url) {
            window.open(url, '_blank')
        } else {
            console.log(`未知社交平台：${name}`)
        }
    }

    const showCoffeeDialog = ref(false)  // 控制咖啡图片 dialog
    const touchMe = (name: string) => {
        const urlMap: Record<string, string> = {
            mailMe: mailMe.linkUrl,
            rssMe: rssMe.linkUrl
        }
        const url = urlMap[name]
        if (url) {
            window.open(url, '_blank')
        }
    }

    onMounted(async () => {
        // 页面加载时，从后端获取文章content
        const result = await axios_server.get('getNoteAllContent/', {
            params: {
                noteListId
            }
        })
        Object.assign(noteStore.currentNote, result.data)

        // 将markdown进行渲染
        noteStore.currentNote.renderedMarkdown = md.render(noteStore.currentNote.markdownContent)

        // 调用 handleTableOfContents 来处理table of contents
        handleTableOfContents()

        // 调用 highlightCode 来处理代码高亮
        highlightCode();

        // 页面挂载时监听handleScroll
        window.addEventListener('scroll', handleScroll)
        const rect = coverImageRef.value!.getBoundingClientRect()
        isScrollOverViewport.value = rect.bottom <= 55
    })

    onUnmounted(() => {
        // 页面卸载时移除监听
        window.removeEventListener('scroll', handleScroll)
    })

    // 解析并高亮代码块
    const highlightCode = () => {
        const codeBlock = document.querySelectorAll('pre code')
        codeBlock.forEach((block) => {
            hljs.highlightElement(block as HTMLElement)
        })
    }

    // 实时渲染 Markdown 内容
    watchEffect(() => {
        if (noteStore.currentNote.renderedMarkdown) {
            setTimeout(() => {
                highlightCode()
            }, 100)
        }
    });
</script>

<style scoped lang='scss'>
    .header-container {
        padding: 0;
        margin: 0;
        position: fixed;
        width: 100%;
        height: 8vh;
        z-index: 1000;

        .header {
            display: flex;
            justify-content: center;
            align-items: stretch;
            height: 100%;
            width: 100%;
            background-color: rgba(100, 100, 100, 0.25);

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
            background-color: rgb(0, 35, 35);
            box-shadow: 5px 0 10px rgba(255, 255, 255, 0.5);
            border-bottom: 1px solid rgba(0, 35, 35, 0.5);
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
            padding: 2px 10px 2px 100px;
            border-radius: 10px 10px 2px 0;
            position: relative;
            top: -8rem;
            left: 20rem;
            font-size: 2rem;
            background-color: rgba(0, 75, 57, 0.75);
            color: #ffffff;
        }
    }

    .article-content-container {
        display: flex;
        justify-content: center;
        align-items: flex-start;

        .article-background {
            padding: 50px 80px 20px 80px;
            width: 75%;
            position: relative;
            top: -8.5em;

            .tags-category-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 12px;

                .tags-container {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;

                    .tag {
                        background-color: rgba(0, 75, 57);
                        color: white;
                        padding: 6px 10px;
                        border-radius: 5px;
                        font-size: 0.8em;
                        font-weight: 800;
                    }
                }

                .category-container {

                    .category {
                        padding: 6px 10px;
                        border-radius: 10px;
                        background-color: white;
                        display: flex;
                        align-items: center;
                        gap: 5px;

                        .category-icon {
                            font-size: 0.8em;
                            color: rgba(0, 75, 57);
                        }

                        .category-text {
                            font-size: 0.8rem;
                            font-weight: 800;
                            color: rgba(0, 75, 57);
                        }
                    }
                }
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
                        color: rgb(20, 100, 90);
                        font-size: 1rem;
                    }

                    .created-date-text {
                        color: rgb(20, 100, 90);
                        font-size: 1rem;
                    }
                }

                .modified-date {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .modified-date-icon {
                        color: rgb(20, 100, 90);
                        font-size: 1rem;
                    }

                    .modified-date-text {
                        color: rgb(20, 100, 90);
                        font-size: 1rem;
                    }
                }

                .viewed {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .viewed-icon {
                        color: rgb(20, 100, 90);
                        font-size: 1rem;
                    }

                    .viewed-text {
                        color: rgb(20, 100, 90);
                        font-size: 1rem;
                    }
                }

                .liked {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .liked-icon {
                        color: rgb(20, 100, 90);
                        font-size: 1rem;
                    }

                    .liked-text {
                        color: rgb(20, 100, 90);
                        font-size: 1rem;
                    }
                }

                .disgusted {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .disgusted-icon {
                        color: rgb(20, 100, 90);
                        font-size: 1rem;
                    }

                    .disgusted-text {
                        color: rgb(20, 100, 90);
                        font-size: 1rem;
                    }
                }
            }

            .divider1 {
                width: 100%;
                height: 2px;
                background-color: rgba(0, 75, 57);
                margin: 10px 0 10px 0;
            }

            .article-body-container {
                display: flex;
                justify-content: center;
                align-items: flex-start;

                .article-body {
                    width: 100%; // 控制文章宽度
                    padding: 15px 25px; // 设置内边距
                    border-radius: 12px; // 给背景添加圆角效果
                }
            }

            .divider2 {
                width: 100%;
                height: 2px;
                background-color: rgba(0, 75, 57);
                margin: 20px 0 20px 0;
            }

            .article-footer-container {
                padding: 15px;
                border-radius: 5px;
                box-shadow: 1px 2px 3px rgba(138, 185, 168, 0.3);
                margin: 30px 0 20px 0;
                background-color: rgba(0, 75, 57, 0.15);;
                border: 1px solid rgba(0, 75, 57);;

                .author-container {
                    .author {
                        display: flex;
                        align-items: center;
                        gap: 1px;
                        margin: 15px;

                        .author-icon {
                            color: rgb(10, 90, 110);
                            font-size: 0.9em;
                        }

                        .author-text {
                            color: rgb(10, 110, 90);
                            font-size: 0.85em;
                            font-weight: 800;
                        }
                    }
                }

                .link-container {
                    .link {
                        display: flex;
                        align-items: center;
                        gap: 2px;
                        margin: 15px;

                        .link-icon {
                            color: rgb(10, 90, 110);
                            font-size: 0.9em;
                        }

                        .link-text {
                            color: rgb(10, 110, 90);
                            font-size: 0.85em;
                            font-weight: 800;
                        }
                    }
                }

                .copy-right-container {
                    .copy-right {
                        display: flex;
                        align-items: center;
                        gap: 4px;
                        margin: 15px;

                        .copy-right-icon {
                            color: rgb(10, 90, 110);
                            font-size: 0.9em;
                        }

                        .copy-right-text {
                            color: rgb(10, 110, 90);
                            font-size: 0.85em;
                            font-weight: 800;
                        }
                    }
                }
            }

            .share-container {
                position: relative;
                display: flex;
                justify-content: space-evenly;
                align-items: center;

                .tags {
                    width: 30%;
                    display: flex;
                    justify-content: flex-start;
                    gap: 10px;
                    position: relative;
                    top: -20px;
                    left: -120px;

                    .tag {
                        background-color: rgba(0, 75, 57);
                        color: white;
                        padding: 6px 10px;
                        border-radius: 5px;
                        font-size: 0.8em;
                        font-weight: 800;
                    }
                }

                .share-icon {
                    width: 30%;
                    display: flex;
                    justify-content: flex-end;
                    padding: 15px;
                    position: relative;
                    top: -12px;
                    left: 150px;

                    .weibo-icon {
                        margin: 0 15px 15px 0;
                        max-width: 10%;
                        cursor: pointer;
                    }

                    .douban-icon {
                        margin: 0 15px 15px 0;
                        max-width: 10%;
                        cursor: pointer;
                    }

                    .zhihu-icon {
                        margin: 0 15px 15px 0;
                        max-width: 10%;
                        cursor: pointer;
                    }

                    .twitter-icon {
                        margin: 0 15px 15px 0;
                        max-width: 10%;
                        cursor: pointer;
                    }

                    .facebook-icon {
                        margin: 0 15px 15px 0;
                        max-width: 10%;
                        cursor: pointer;
                    }

                    .github-icon {
                        margin: 0 15px 15px 0;
                        max-width: 10%;
                        cursor: pointer;
                    }

                    .shaoshupai-icon {
                        margin: 0 15px 15px 0;
                        max-width: 10%;
                        cursor: pointer;
                    }
                }
            }

            .coffee-container {
                position: relative;
                top: -10px;
                display: flex;
                justify-content: center;
                align-items: center;
                cursor: pointer;

                .coffee-icon {
                    max-width: 2.5%;
                }

                .coffee-text {
                    color: rgb(10, 110, 90);
                    font-size: 1rem;
                    font-weight: 800;
                }
            }
        }
    }

    .divider3 {
        position: relative;
        top: -75px;
        display: flex;
        width: 100%;
        height: 2px;
        background-color: #515c7a;;
        margin: 10px 0 10px 0;
    }


    @import "@/styles/markdown";
    :deep(.markdown-content) {
    }

    :deep(.toc) {
    }

    .qr-card {
        border-radius: 12px;
        padding: 1rem;

        .v-card-title {
            font-size: 1.2rem;
            font-weight: bold;
        }

        .v-card-text img {
            border-radius: 8px;
            max-width: 100%;
        }
    }

</style>