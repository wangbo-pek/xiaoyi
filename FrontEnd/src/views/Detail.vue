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

    <div class="article-subtitle-container">
        <span class="article-subtitle">{{ noteStore.currentNote.subtitle }}</span>
    </div>

    <div class="article-content-container">
        <div class="article-background">

            <!-- 标签、二级分类区域 -->
            <div class="tags-classification-container">
                <div class="tags-container">
                    <span class="tag" v-for="(tag, index) in noteStore.currentNote.tagsName" :key="index">
                        {{ tag }}
                    </span>
                </div>
                <div class="classification-container">
                    <span class="classification">
                        <v-icon class="classification-icon" icon="mdi-bookmark-multiple"></v-icon>
                        <span class="first-classification-text">{{ noteStore.currentNote.firstClassification }}</span>
                        <span> / </span>
                        <span class="second-classification-text">{{ noteStore.currentNote.secondClassification }}</span>
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
                    <v-img class="wechat-icon"
                           :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/wechat.svg'"></v-img>
                    <v-img class="twitter-icon"
                           :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/twitter.svg'"></v-img>
                    <v-img class="github-icon"
                           :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/github.svg'"></v-img>
                    <v-img class="google-plus-icon"
                           :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/google_plus.svg'"></v-img>
                    <v-img class="linkedin-icon"
                           :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/linkedin.svg'"></v-img>
                    <v-img class="weibo-icon"
                           :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/weibo.svg'"></v-img>
                    <v-img class="zhihu-icon"
                           :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/zhihu.svg'"></v-img>
                </div>
            </div>

            <div class="coffee-container">
                <span class="coffee-text">COFFEE ME &nbsp;</span>
                <v-img class="coffee-icon"
                       :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/coffee.svg'"></v-img>
            </div>
        </div>
    </div>

    <div class="recommend-note-container">
        222
    </div>

</template>

<script setup lang='ts'>
    import {useRoute} from "vue-router";
    import {onMounted, onUnmounted, ref, watchEffect} from "vue";
    import useNoteStore from "@/store/note.ts";
    import axios_server from "@/utils/axios_server.ts";
    import HeaderNav from "@/components/Header/HeaderNav.vue";
    import HeaderTitle from "@/components/Header/HeaderTitle.vue";
    import HeaderWidget from "@/components/Header/HeaderWidget.vue";
    import MarkdownIt from 'markdown-it';
    import hljs from 'highlight.js'
    import 'highlight.js/styles/github.css'

    defineOptions({
        name: 'Detail',
        inheritAttrs: false
    })

    const md = new MarkdownIt({
        html: true
    })
    const route = useRoute()
    const noteStore = useNoteStore()
    const noteListId = Number(route.params.id)

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

    onMounted(async () => {
        // 页面加载时，从后端获取文章content
        const result = await axios_server.get('getNoteAllContent/', {
            params: {
                noteListId
            }
        })
        console.log('result ~~~~~')
        console.log(result)
        Object.assign(noteStore.currentNote, result.data)

        // 将markdown进行渲染，渲染为html
        noteStore.currentNote.renderedMarkdown = md.render(noteStore.currentNote.markdownContent)
        console.log('renderedMarkdown ~~~~~~ ')
        console.log(noteStore.currentNote.renderedMarkdown)

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
            top: -1100%;
            left: 15%;
            font-size: 1.5rem;
            background-color: rgba(58, 136, 136, 0.75);
            color: #cccccc;
        }
    }

    .article-subtitle-container {

        .article-subtitle {
            padding: 10px 10px 10px 300px;
            border-radius: 2px 2px 2px 10px;
            position: relative;
            top: -1130%;
            left: 20%;
            font-size: 1.3rem;
            background-color: rgba(238, 238, 238, 0.75);
            color: #113c46;
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
                        font-size: 0.8em;
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
                            font-size: 0.8em;
                            color: #113c46;
                        }

                        .first-classification-text {
                            font-size: 0.8rem;
                            font-weight: 700;
                            color: #113c46;
                        }

                        .second-classification-text {
                            font-size: 0.8rem;
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
                margin: 10px 0 10px 0;
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
                        color: #8ab9a8;
                        font-size: 1rem;
                    }

                    .created-date-text {
                        color: #8ab9a8;
                        font-size: 1rem;
                    }
                }

                .modified-date {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .modified-date-icon {
                        color: #8ab9a8;
                        font-size: 1rem;
                    }

                    .modified-date-text {
                        color: #8ab9a8;
                        font-size: 1rem;
                    }
                }

                .viewed {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .viewed-icon {
                        color: #8ab9a8;
                        font-size: 1rem;
                    }

                    .viewed-text {
                        color: #8ab9a8;
                        font-size: 1rem;
                    }
                }

                .liked {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .liked-icon {
                        color: #8ab9a8;
                        font-size: 1rem;
                    }

                    .liked-text {
                        color: #8ab9a8;
                        font-size: 1rem;
                    }
                }

                .disgusted {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .disgusted-icon {
                        color: #8ab9a8;
                        font-size: 1rem;
                    }

                    .disgusted-text {
                        color: #8ab9a8;
                        font-size: 1rem;
                    }
                }
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
                background-color: #515c7a;;
                margin: 20px 0 20px 0;
            }

            .article-footer-container {
                padding: 15px;
                border-radius: 5px;
                box-shadow: 1px 2px 3px rgba(138, 185, 168, 0.3);
                margin: 30px 0 20px 0;
                background-color: rgba(138, 185, 168, 0.1);
                border: 1px solid rgba(138, 185, 168, 0.5);

                .author-container {
                    .author {
                        display: flex;
                        align-items: center;
                        gap: 1px;
                        margin: 15px;

                        .author-icon {
                            color: #8ab9a8;
                            font-size: 0.9em;
                        }

                        .author-text {
                            color: #8ab9a8;
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
                            color:#8ab9a8;
                            font-size:  0.9em;
                        }

                        .link-text {
                            color: #8ab9a8;
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
                            color: #8ab9a8;
                            font-size:  0.9em;
                        }

                        .copy-right-text {
                            color: #8ab9a8;
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
                            background-color: #113c46;
                            color: white;
                            padding: 6px 10px;
                            border-radius: 5px;
                            font-size: 0.8em;
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

                        .wechat-icon {
                            margin: 0 15px 15px 0;
                            max-width: 10%;
                        }

                        .twitter-icon {
                            margin: 0 15px 15px 0;
                            max-width: 10%;
                        }

                        .github-icon {
                            margin: 0 15px 15px 0;
                            max-width: 10%;
                        }

                        .google-plus-icon {
                            margin: 0 15px 15px 0;
                            max-width: 10%;
                        }

                        .linkedin-icon {
                            margin: 0 15px 15px 0;
                            max-width: 10%;
                        }

                        .weibo-icon {
                            margin: 0 15px 15px 0;
                            max-width: 10%;
                        }

                        .zhihu-icon {
                            margin: 0 15px 15px 0;
                            max-width: 10%;
                        }

                    }
                }

            .coffee-container {
                    position: relative;
                    top: -10px;
                    display: flex;
                    justify-content: center;
                    align-items: center;

                    .coffee-icon {
                        max-width: 2.5%;
                    }

                    .coffee-text {
                        color: #c3effa;
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

    .change-bgcolor {
        background-color: #113c46;
    }

    @import "@/styles/markdown";
    :deep(.markdown-content) {
    }

    :deep(.toc) {
    }

</style>