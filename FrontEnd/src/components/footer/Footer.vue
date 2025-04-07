<template>
    <div class="footer-container">
        <div class="copy-right">
            <div class="first-line">
                <span class="info-text">Copyright</span>
                <v-icon class="info-icon" icon="mdi-copyright"></v-icon>
                <span class="info-text">2023 - 2025 &nbsp;&nbsp;</span>
                <span class="info-text strong-text">{{ blogStore.blogInfo.myName }}</span>
                <span class="info-text">&nbsp;&nbsp;|&nbsp;&nbsp;Powered By </span>
                <span class="info-text strong-text">Django + Vue</span>
            </div>
            <div class="second-line">
                <v-icon class="info-icon" icon="mdi-text-long"></v-icon>
                <span class="info-text">站点总文章数：</span>
                <span class="info-text strong-text">{{ blogStore.blogInfo.blogArticlesCount }}篇</span>
                <span class="info-text">&nbsp;&nbsp;|&nbsp;&nbsp;</span>
                <v-icon class="info-icon" icon="mdi-chart-areaspline"></v-icon>
                <span class="info-text">站点总字数：</span>
                <span class="info-text strong-text">{{ blogStore.blogInfo.blogWordsCount }}字</span>
                <span class="info-text">&nbsp;&nbsp;|&nbsp;&nbsp;</span>
                <v-icon class="info-icon" icon="mdi-eye-outline"></v-icon>
                <span class="info-text">总访问量：</span>
                <span class="info-text strong-text">{{ blogStore.blogInfo.blogViewedCount }}人</span>
                <span class="info-text">&nbsp;&nbsp;|&nbsp;&nbsp;</span>
                <v-icon class="info-icon" icon="mdi-cloud-outline"></v-icon>
                <span class="info-text">本站已运行：</span>
                <span class="info-text strong-text">{{ blogStore.blogInfo.blogDurationRunning }}天</span>
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

    </div>
</template>

<script setup lang='ts'>
    import useBlogStore from "@/store/blog.ts";

    defineOptions({
        name: 'Footer',
        inheritAttrs: false
    })

    const blogStore = useBlogStore()
</script>

<style scoped lang='scss'>
    .footer-container {
        background-color: rgb(0, 35, 35);
        box-shadow: 5px 0 10px rgba(255, 255, 255, 0.5);
        border-top: 1px solid rgba(0, 35, 35, 0.5);
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;

        .copy-right {
            width: 50%;

            .first-line,
            .second-line,
            .third-line {
                color: rgba(255, 255, 255, 0.75);
                width: 100%;
                max-width: 600px;
                text-align: left;
                padding: 5px;
                box-sizing: border-box;
                font-size: 0.75rem;
            }

            .first-line {
                margin: 30px 5px 5px 5px;
            }

            .second-line {
                margin-bottom: 30px;
            }

            .info-text {
                vertical-align: middle;
                font-size: 0.85rem;
            }

            .info-icon {
                font-size: 0.7rem;
                position: relative;
                top: 1px;
                margin: 0 2px;
            }

            .strong-text {
                font-weight: 800;
            }
        }

        .touch-me {
            display: flex;
            justify-content: left;
            align-items: center;
            width: 15%;

            .wechat-icon {
                margin: 0 10px 0 10px;
                max-width: 1.8rem;
            }

            .mail-icon {
                margin: 0 10px 0 10px;
                max-width: 1.8rem;
            }

            .twitter-icon {
                margin: 0 10px 0 10px;
                max-width: 1.8rem;
            }
        }
    }

</style>