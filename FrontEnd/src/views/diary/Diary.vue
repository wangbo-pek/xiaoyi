<template>

    <div class="container">
        <div class="diary-timeline">
            <v-timeline class="diary-timeline" align="start" line-color="rgba(255, 255, 255, 0.5)">
                <v-timeline-item
                    v-for="(diary, index) in diaryStore.diaryList"
                    :key="index"
                    :dot-color="diary.timelineColor.pointColor"
                    size="small"
                    fill-dot
                    @click="jumpToDiaryDetail(diary.diaryListId)"
                >
                    <template v-slot:opposite>
                        <div class="diary-date" :style="{color:diary.timelineColor.textColor}">
                            <v-chip class="diary-date-chip" variant="tonal" label
                                    :style="{color:diary.timelineColor.textColor}">
                                {{ diary.createdTime }}
                                「 {{ diary.title }} 」
                            </v-chip>
                        </div>
                    </template>
                    <div class="diary-item" :style="{background:diary.timelineColor.pointColor}">
                        <div class="cover-container">
                            <v-img
                                class="cover"
                                cover
                                :src="diary.coverImg"
                            ></v-img>
                        </div>
                        <div class="brief-container">
                            <p class="brief-text">{{ diary.brief }}</p>
                        </div>
                    </div>
                </v-timeline-item>
            </v-timeline>
        </div>
    </div>

</template>

<script setup lang='ts'>
    import {onMounted, onUnmounted} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";
    import useDiaryStore from "@/store/diary.ts";
    import {useRouter} from "vue-router";

    defineOptions({
        name: 'Diary',
        inheritAttrs: false
    })

    const $router = useRouter()
    let appearanceStore = useAppearanceStore()
    let diaryStore = useDiaryStore()

    const jumpToDiaryDetail =  (diaryListId: number) => {
         $router.push({
            name: 'diaryDetail',
            params: {
                id: diaryListId
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

<style scoped lang='scss'>

    .container {
        display: flex;
        justify-content: center;
        position: relative;
        margin-bottom: 100px;
        z-index: 1;

        .diary-timeline {
            position: relative;
            top: 2rem;
            padding: 0 25px 25px 25px;
            transition: transform 0.3s ease;

            .diary-item {
                max-width: 300px;
                border-radius: 5px;
                padding: 20px;
                margin-bottom: 50px;
                box-shadow: 2px 2px 2px rgba(171, 171, 171, 0.25);
                cursor: pointer;
                transition: transform 0.3s ease, box-shadow 0.3s ease;

                &:hover {
                    transform: scale(1.05);
                    box-shadow: 8px 8px 15px rgba(0, 0, 0, 0.35);
                    z-index: 1;
                }

                .cover-container {
                    display: flex;
                    justify-content: center;

                    .cover {
                        border-radius: 10px;
                        border: 1px solid rgba(255, 255, 255, 0.2);
                        box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.25);
                    }
                }

                .brief-container {
                    margin-top: 15px;

                    .brief-text {
                        text-align: left;
                        color: #5a9b9b;
                        font-size: 1rem;
                    }
                }
            }
        }
    }

    .diary-date-chip {
        font-size: 1rem;
    }

</style>