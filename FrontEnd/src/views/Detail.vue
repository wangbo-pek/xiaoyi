<template>
    <div class="detail-container">
        <div class="detail-header">
            <h1>{{ noteContentItem.title }}</h1>
            <div class="detail-meta">
                <span>分类：{{ noteContentItem.firstClassification }} >> {{ noteContentItem.secondClassification }}</span><br>
                <span>标签：{{ noteContentItem.tagsName.join(',') }}</span><br>
                <span>创建时间：{{ noteContentItem.createdTime }}</span><br>
                <span>修改时间：{{ noteContentItem.modifiedTime }}</span>
            </div>
        </div>
        <img :src="noteContentItem.coverImg" alt="1">
        <div class="detail-content">
            {{ noteContentItem.content }}
        </div>
        <div class="detail-footer">
            <v-btn variant="outlined" @click="goBack">返回</v-btn>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import {useRoute, useRouter} from "vue-router";
    import {onMounted, reactive} from "vue";
    import useNoteStore from "@/store/note.ts";
    import axios_server from "@/utils/axios_server.ts";
    import type {NoteContentItem} from "@/store/types/note.ts";

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
    })

    const goBack = () => {
        $router.back()
    }

</script>

<style scoped lang='scss'>
    .detail-container {
        max-width: 800px; /* 页面最大宽度 */
        margin: 80px auto 40px; /* 上下左右边距 */
        padding: 24px; /* 内容内边距 */
        background: #ffffff; /* 背景色 */
        border-radius: 12px; /* 圆角 */
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08); /* 阴影 */
        font-family: 'Helvetica Neue', sans-serif; /* 字体 */

        /* 顶部区域样式 */
        .detail-header {
            margin-bottom: 24px;

            h1 {
                font-size: 32px; /* 标题字号 */
                margin-bottom: 8px;
                color: #333;
            }

            .detail-meta {
                font-size: 14px;
                color: #666;

                span {
                    margin-right: 20px; /* 标签之间的间距 */
                }
            }
        }

        /* 正文区域样式 */
        .detail-content {
            font-size: 16px;
            color: #444;
            line-height: 1.8;
            word-break: break-word; /* 防止长词溢出 */

            p {
                margin-bottom: 1em; /* 段落之间的间距 */
            }
        }

        /* 底部返回按钮 */
        .detail-footer {
            text-align: right;
            margin-top: 40px;
        }
    }
</style>