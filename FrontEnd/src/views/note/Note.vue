<template>
    <div class="content-container">
        <div class="article-list">
            <v-row>
                <v-col v-for="(item, index) in noteStore.noteList" :key="index">
                    <div class="article-card">
                        <v-card elevation="14" rounded="lg" hover @click="jumpTo(item.noteListId)">
                            <template v-slot:image>
                                <v-img class="article-img" :src="item.coverImg" cover></v-img>
                            </template>
                            <v-card-item>
                                <v-card-text class="title">{{ item.title }}</v-card-text>
                                <v-card-text class="subtitle">{{ item.brief }} ... ...</v-card-text>
                            </v-card-item>
                            <v-card-item>
                                <template v-for="(subItem) in item.tagsName">
                                    <v-chip class="tags" label variant="text">
                                        <v-icon icon="mdi-label-outline" start></v-icon>
                                        {{ subItem }}
                                    </v-chip>
                                </template>
                            </v-card-item>
                            <v-card-item>
                                <v-chip class="info" label variant="outlined">
                                    <v-icon icon="mdi-thumb-up-outline" start></v-icon>
                                    33
                                </v-chip>
                                <v-chip class="info" label variant="outlined">
                                    <v-icon icon="mdi-thumb-down-outline" start></v-icon>
                                    23
                                </v-chip>
                                <v-chip class="info" label variant="outlined">
                                    <v-icon icon="mdi-heart-outline" start></v-icon>
                                    23
                                </v-chip>
                            </v-card-item>
                        </v-card>
                    </div>
                </v-col>
            </v-row>
        </div>
    </div>


</template>

<script setup lang='ts'>
    import useNoteStore from "@/store/note.ts";
    import {useRouter} from "vue-router";
    import {onMounted, onUnmounted} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";

    defineOptions({
        name: 'Note',
        inheritAttrs: false
    })

    const noteStore = useNoteStore()
    const $router = useRouter()
    let appearanceStore = useAppearanceStore()

    const jumpTo = (noteListId: number) => {
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

        .function-bar {
            position: fixed;
            top: 50px;
            left: 6%;
            width: 74%;
            height: 10%;
            background-color: rgba(23, 104, 122, 0.75);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
            border-radius: 10px;

            .select-container {
                position: relative;
                top: 10px;
                left: 0;
                width: 400px;
                margin: 0 10px;
            }

        }

        .article-list {
            position: relative;
            top: 6vh;
            left: 2vw;
            width: 100%;
            margin: 0 auto;
            padding: 10px 2px;
            border-radius: 5px;
            min-height: 200px;
            box-sizing: border-box;

            .article-card {
                //margin: 20px;

                .v-card {
                    width: 300px;
                    height: 300px;
                    border: 1px solid rgba(21, 110, 78, 0.9);
                    box-shadow: 2px 6px 12px rgba(21, 110, 78, 0.9);
                    transition: transform 0.3s ease;

                    &:hover {
                        transform: scale(1.03);
                    }
                }

                .article-img {
                    border-bottom: 3px solid #ff0000;
                    filter: brightness(0.3);
                }

                .title {
                    font-size: 16px;
                    padding: 20px;
                    font-weight: 800;
                    color: white;
                }

                .subtitle {
                    font-size: 14px;
                    padding: 16px;
                    font-weight: 300;
                    color: #d2d2d2;
                }

                .tags {
                    font-size: 13px;
                    margin: 0 1px;
                    color: white;
                }

                .info {
                    margin: 0 5px;
                    color: white;
                }
            }

        }
    }

</style>