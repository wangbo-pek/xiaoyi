<template>
    <div class="content-container">
        <div class="function-bar">function-bar</div>
        <div class="article-list">
            <v-row>
                <v-col v-for="(item, index) in noteStore.noteList" :key="index">
                    <div class="article-card">
                        <v-card elevation="14" rounded="lg" hover>
                            <v-img class="article-img" :src="item.coverImg" cover>
                                <v-card-title>
                                    <span>{{ item.title }}</span>
                                </v-card-title>
                            </v-img>
                            <v-card-text>
                                {{ item.brief }}
                            </v-card-text>
                            <v-card-actions>
                                <v-btn class="my-btn" variant="text">查看</v-btn>
                                <v-btn class="my-btn" variant="text">删除</v-btn>
                            </v-card-actions>
                        </v-card>
                    </div>
                </v-col>
            </v-row>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import useNoteStore from "@/store/note.ts";

    defineOptions({
        name: 'Note',
        inheritAttrs: false
    })

    const noteStore = useNoteStore()

</script>

<style scoped lang="scss">
    .content-container {
        position: relative;
        width: 100%;
        height: 100%;

        .function-bar {
            position: fixed;
            top: 85px;
            left: 12%;
            width: 65%;
            height: 8%;
            background-color: #f5f5dc;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        .article-list {
            position: relative;
            top: 10%;
            width: 98%;
            margin: 0 auto;
            background-color: lightyellow;
            padding: 10px;
            border: 1px solid #cccccc;
            border-radius: 5px;
            min-height: 200px;
            box-sizing: border-box;

            .article-card {
                width: 350px;
                margin: 10px auto;

                .v-card {
                    border: 2px solid rgba(21, 110, 78, 0.9);
                    box-shadow: 2px 6px 12px rgba(21, 110, 78, 0.9);
                    transition: transform 0.3s ease;

                    &:hover {
                        transform: scale(1.03);
                    }
                }

                .article-img {
                    height: 200px;
                    border-bottom: 3px solid #28936d;
                    filter: brightness(0.9);
                }

                .v-card-title {
                    font-size: 20px;
                    padding: 16px;
                    font-weight: 800;

                    span {
                        background-color: rgba(2, 2, 2, 0.3);
                        color: #f5f5f5;
                        padding: 0 10px;
                        border-radius: 5px;
                    }
                }

                .v-card-text {
                    font-size: 16px;
                    padding: 16px;
                    font-weight: 300;
                    color: #727272;
                }

                .v-card-action {
                    justify-content: flex-end;
                    padding: 8px 16px;
                }

                .my-btn {
                    width: 65px;
                    font-size: 14px;
                    color: #d7d7d7;
                    margin: 0 3px;
                    background-color: rgba(42, 6, 6, 0.45)
                }
            }
        }
    }

</style>