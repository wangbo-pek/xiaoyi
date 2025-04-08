<template>
    <div class="sider-container">
        <div class="introduction" @click="jumpToAbout">
            <div class="my-avatar">
                <v-img class="my-avatar-icon"
                       :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/my_only_girl.png'"></v-img>
            </div>
            <div class="my-name">
                <span class="my-name-text">{{ wang.nickName }}</span>
            </div>

            <div class="my-short-intro">
                <div class="my-short-intro-text">
                    {{ wang.shortIntro }}
                </div>
            </div>

        </div>
        <div class="touch-me">
            <v-img class="wechat-icon" :src="wechatMe.svgIconUrl" @click="showWechatDialog = true"></v-img>
            <v-img class="mail-icon" :src="mailMe.svgIconUrl" @click="touchMe(mailMe.name)"></v-img>
            <v-img class="rss-icon" :src="rssMe.svgIconUrl" @click="touchMe(rssMe.name)"></v-img>
        </div>
        <div class="coffee-container" @click="showCoffeeDialog = true">
            <span class="coffee-text">{{ coffeeMe.title }} &nbsp;</span>
            <v-img class="coffee-icon" :src="coffeeMe.svgIconUrl"></v-img>
        </div>
    </div>

    <!-- 我的微信二维码 -->
    <v-dialog v-model="showWechatDialog" width="500">
        <v-card class="qr-card" color="#1e1e1e">
            <v-card-title class="text-center text-white">微信扫一扫</v-card-title>
            <v-card-text class="text-center">
                <v-img
                    :src="wechatMe.wechatInfo"
                    aspect-ratio="1"
                    contain
                />
            </v-card-text>
            <v-card-actions class="justify-center">
                <v-btn color="rgb(242, 204, 15)" @click="showWechatDialog = false">关闭</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

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
    import {useRouter} from "vue-router"
    import {ref} from "vue";
    import {wang, mailMe, rssMe, wechatMe, coffeeMe} from '@/data/personalDetail.ts'

    defineOptions({
        name: 'Sider',
        inheritAttrs: false
    })

    const $router = useRouter()
    const showWechatDialog = ref(false)  // 控制微信二维码 dialog
    const showCoffeeDialog = ref(false)  // 控制咖啡图片 dialog

    const jumpToAbout = () => {
        $router.push({
            name: 'about',
        })
    }

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

</script>

<style scoped lang='scss'>
    .sider-container {
        position: relative;
        width: 100%;
        height: 100%;

        .introduction {
            text-align: center;
            position: relative;
            top: 5rem;
            width: 100%;
            cursor: pointer;

            .my-avatar {
                display: flex;
                justify-content: center;

                .my-avatar-icon {
                    max-width: 5rem;
                }
            }

            .my-name {
                margin: 10px 0 10px 0;

                .my-name-text {
                    color: white;
                    font-size: 1.5rem;
                    font-weight: 200;
                }
            }

            .my-short-intro {
                display: flex;
                justify-content: center;
                margin: 10px 0 10px 0;

                .my-short-intro-text {
                    color: white;
                    max-width: 15rem;
                    font-size: 0.8rem;
                    font-weight: 700;
                    text-align: left;
                    line-height: 20px;
                }
            }
        }

        .touch-me {
            position: relative;
            top: 5.5rem;
            width: 100%;
            display: flex;
            justify-content: center;
            margin-top: 20px;

            .wechat-icon {
                margin: 0 15px 0 15px;
                max-width: 1.8rem;
                cursor: pointer;
            }

            .mail-icon {
                margin: 0 15px 0 15px;
                max-width: 1.8rem;
                cursor: pointer;
            }

            .rss-icon {
                margin: 0 15px 0 15px;
                max-width: 1.8rem;
                cursor: pointer;
            }
        }

        .coffee-container {
            position: relative;
            top: 7.5rem;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;

            .coffee-icon {
                max-width: 10%;
            }

            .coffee-text {
                color: rgb(0, 200, 250);
                font-size: 1rem;
                font-weight: 800;
            }
        }
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