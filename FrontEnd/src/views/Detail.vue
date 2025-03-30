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
                <div class="article-body markdown-content" v-html="renderedMarkdown"></div>
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

        </div>
    </div>

    <div class="share-container"></div>
    <div class="coffee-me-container"></div>
    <div class="recommend-note-container"></div>

</template>

<script setup lang='ts'>
    import {useRoute, useRouter} from "vue-router";
    import {onMounted, onUnmounted, reactive, ref, watchEffect} from "vue";
    import useNoteStore from "@/store/note.ts";
    import axios_server from "@/utils/axios_server.ts";
    import type {NoteContentItem} from "@/store/types/note.ts";
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
    let markdownContent = ref('')
    let renderedMarkdown = ref('');
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
        "markdownContent": '',
        "htmlContent": '',
        "imageUrls": []
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
        noteContentItem.markdownContent = content.data.markdownContent
        noteContentItem.htmlContent = content.data.htmlContent
        noteContentItem.imageUrls = content.data.imageUrls

        markdownContent.value = noteContentItem.markdownContent
        markdownContent.value = md.renderInline(content.data.markdownContent)
        renderedMarkdown = ref('')

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

    // 解析并高亮代码块
    const highlightCode = () => {
        const codeBlock = document.querySelectorAll('pre code')
        codeBlock.forEach((block) => {
            hljs.highlightElement(block as HTMLElement)
        })
    }

    // 实时渲染 Markdown 内容
    watchEffect(() => {
        renderedMarkdown.value = md.render(markdownContent.value)
        // 提取生成的目录
        if (renderedMarkdown.value) {
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
        z-index: 900;

        .article-background {
            padding: 50px 80px 20px 80px;
            width: 75%;
            position: relative;
            top: -3%;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px 10px 10px 10px;
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
                        color: #515c7a;
                        font-size: 1rem;
                    }

                    .created-date-text {
                        color: #515c7a;
                        font-size: 1rem;
                    }
                }

                .modified-date {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .modified-date-icon {
                        color: #515c7a;
                        font-size: 1rem;
                    }

                    .modified-date-text {
                        color: #515c7a;
                        font-size: 1rem;
                    }
                }

                .viewed {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .viewed-icon {
                        color: #515c7a;
                        font-size: 1rem;
                    }

                    .viewed-text {
                        color: #515c7a;
                        font-size: 1rem;
                    }
                }

                .liked {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .liked-icon {
                        color: #515c7a;
                        font-size: 1rem;
                    }

                    .liked-text {
                        color: #515c7a;
                        font-size: 1rem;
                    }
                }

                .disgusted {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .disgusted-icon {
                        color: #515c7a;
                        font-size: 1rem;
                    }

                    .disgusted-text {
                        color: #515c7a;
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
                box-shadow: 0 2px 5px rgba(150, 150, 150, 0.3);
                //display: flex;
                flex-wrap: wrap;
                //gap: 15px;
                margin: 30px 0 20px 0;
                background-color: rgba(250, 250, 250, 0.2);
                border: 1px solid rgba(150, 150, 150, 0.3);

                .author-container {
                    .author {
                        display: flex;
                        align-items: center;
                        gap: 1px;
                        margin: 15px;

                        .author-icon {
                            color: #113c46;
                            font-size: 0.8em;
                        }

                        .author-text {
                            color: #113c46;
                            font-size: 0.8em;
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
                            color: #113c46;
                            font-size: 0.8em;
                        }

                        .link-text {
                            color: #113c46;
                            font-size: 0.8em;
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
                            color: #113c46;
                            font-size: 0.8em;
                        }

                        .copy-right-text {
                            color: #113c46;
                            font-size: 0.8em;
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

    /* 样式调整：设置 Markdown 中的图片样式 */
    :deep(.markdown-content img) {
        max-width: 90%; // 限制图片宽度为容器的最大宽度的 90%
        display: block; // 将图片设置为块级元素
        margin: 20px auto; // 上下边距 20px，左右居中
        border-radius: 5px; // 添加圆角效果
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); // 给图片添加阴影效果
    }

    /* 设置 markdown-content 中的 h1 ~ h4 标题样式 */
    :deep(.markdown-content h1) {
        font-size: 2em; // 设置 h1 字体大小
        color: #003366; // 设置 h1 字体颜色
        margin: 30px 0; // 设置上下间距
        font-weight: 800; // 设置加粗
        text-align: center; // 设置居中对齐
    }

    :deep(.markdown-content h2) {
        font-size: 1.75em; // 设置 h2 字体大小
        color: #005b99; // 设置 h2 字体颜色
        margin: 20px 0; // 设置上下间距
        font-weight: 700; // 设置加粗
    }

    :deep(.markdown-content h3) {
        font-size: 1.5em; // 设置 h3 字体大小
        color: #007bb5; // 设置 h3 字体颜色
        margin: 16px 0; // 设置上下间距
        font-weight: 600; // 设置加粗
        text-align: left; // 设置左对齐
    }

    :deep(.markdown-content h4) {
        font-size: 1.25em; // 设置 h4 字体大小
        color: #0099cc; // 设置 h4 字体颜色
        margin: 15px 0; // 设置上下间距
        font-weight: 400; // 设置加粗
        text-align: left; // 设置左对齐
    }

    /* 设置 markdown-content 中的段落样式 */
    :deep(.markdown-content p) {
        font-size: 16px; // 设置段落字体大小
        color: #555555; // 设置段落字体颜色
        line-height: 1.5; // 设置行高
        margin: 10px 0; // 设置上下边距
        padding: 0 10px; // 设置左右内边距
        text-align: justify; // 设置文本对齐方式，自动调整左右边距
    }

    /* 设置无序列表（ul）样式 */
    :deep(.markdown-content ul) {
        list-style-type: disc; /* 使用圆点样式 */
        padding-left: 50px; /* 给无序列表增加左边距 */
        margin: 10px 0; /* 给无序列表设置上下间距 */
    }

    /* 设置无序列表项（li）样式 */
    :deep(.markdown-content ul li) {
        font-size: 16px; /* 设置字体大小 */
        color: #555555; /* 设置文本颜色 */
        margin-bottom: 8px; /* 设置列表项之间的间距 */
        line-height: 1.6; /* 设置行高 */
    }

    /* 设置有序列表（ol）样式 */
    :deep(.markdown-content ol) {
        list-style-type: decimal; /* 使用数字样式 */
        padding-left: 50px; /* 给有序列表增加左边距 */
        margin: 10px 0; /* 给有序列表设置上下间距 */
    }

    /* 设置有序列表项（li）样式 */
    :deep(.markdown-content ol li) {
        font-size: 16px; /* 设置字体大小 */
        color: #555555; /* 设置文本颜色 */
        margin-bottom: 8px; /* 设置列表项之间的间距 */
        line-height: 1.6; /* 设置行高 */
    }

    /* 设置代码块的背景颜色、内边距、圆角和阴影效果 */
    :deep(.markdown-content pre) {
        font-size: 0.95rem; /* 调整字体大小 */
        line-height: 1.6; /* 增加行高 */
        font-family: 'Courier New', Courier, monospace;
        background-color: #f5f5f5; /* 轻灰色背景 */
        padding: 15px; /* 添加内边距 */
        border-radius: 8px; /* 圆角效果 */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* 阴影效果 */
        overflow-x: auto; /* 超出宽度时，出现水平滚动条 */
    }

    /* 设置代码块内部代码的样式 */
    :deep(.markdown-content code) {
        font-family: 'Fira Code', Courier, monospace; /* 等宽字体 */
        font-size: 0.9rem; /* 字体大小 */
        background-color: #f5f5f5; /* 背景色与pre背景一致 */
        padding: 2px 6px; /* 小的内边距 */
        border-radius: 5px; /* 圆角效果 */
        color: #d9534f; /* 代码内容的颜色 */
    }

    /* 自定义关键字样式 */
    :deep(.markdown-content .hljs-keyword) {
        color: #d58052; /* 关键字使用红色 */
        font-weight: bold;
    }

    /* 自定义字符串样式 */
    :deep(.markdown-content .hljs-string) {
        color: #276751; /* 字符串使用蓝色 */
    }

    /* 自定义函数名样式 */
    :deep(.markdown-content .hljs-function) {
        color: #f0ad4e; /* 函数名使用黄色 */
    }

    /* 自定义斜体样式 */
    :deep(.markdown-content em) {
        font-style: italic;
        color: #626262; /* 你可以设置其他颜色 */
    }

    /* 下划线样式 */
    :deep(.markdown-content u) {
        text-decoration: underline;
        color: #626262; /* 下划线文本的颜色 */
        font-weight: 700;
    }

    /* 删除线样式 */
    :deep(.markdown-content del) {
        text-decoration: line-through;
        color: #a2a2a2; /* 删除线文本的颜色 */
    }

    /* 引用样式 */
    :deep(.markdown-content blockquote) {
        padding: 10px 20px; /* 给引用框添加内边距 */
        border-left: 5px solid #3fb2ae; /* 添加左侧边框来区分引用 */
        background-color: rgba(63, 178, 174, 0.2); /* 设置背景颜色 */
        margin: 15px 0; /* 设置上下外边距 */
        font-weight: 800;
    }

    /* 引用样式 */
    :deep(.markdown-content blockquote p) {
        color: #1c4948; /* 引用文本的颜色 */
        font-weight: 800;
        margin: 0; /* 移除引用内部段落的默认外边距 */
    }
</style>
