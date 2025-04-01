<template>
    <div class="container">

        <div class="diary-timeline">
            <v-timeline class="diary-timeline" align="start">
                <v-timeline-item
                    v-for="(diary, i) in testDiaryList"
                    :key="i"
                    :dot-color="diary.timelinePointColor"
                    size="small"
                    fill-dot
                >
                    <template v-slot:opposite>
                        <div class="diary-date" :style="{color:diary.timelinePointColor}">
                            <v-chip class="diary-date-chip" variant="tonal" label :style="{color:diary.timelinePointColor}">
                                {{ diary.createdTime }}
                                &nbsp;
                                {{ diary.title }}
                            </v-chip>
                        </div>
                    </template>
                    <div class="diary-item" :style="{background:diary.timelinePointColor}">
                        <div class="cover-container">
                            <v-img
                                class="cover"
                                :width="400"
                                cover
                                src="https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/note_covers/mcp1/cover.jpg"
                            ></v-img>
                        </div>
                        <div class="brief-container">
                            <p class="brief-text">{{ diary.brief }}... ...</p>
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
    import testDiaryList from "@/mock/diaryMock.ts";

    defineOptions({
        name: 'Diary',
        inheritAttrs: false
    })

    let appearanceStore = useAppearanceStore()


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

        .diary-timeline {
            position: relative;
            top: 2rem;
            padding: 0 25px 25px 25px;

            .diary-item {
                border-radius: 5px;
                padding: 30px;
                margin-bottom: 50px;
                box-shadow: 5px 5px 5px rgba(98, 98, 98, 0.5);

                .diary-info-container {

                    .weather {
                    }

                    .motion {

                    }
                }

                .cover-container {
                    display: flex;
                    justify-content: center;
                    .cover {
                        border-radius: 5px;
                        border: 5px solid white;
                        box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.25);
                    }
                }

                .brief-container {
                    margin-top: 15px;

                    .brief-text {
                        text-align: left;
                        color: white;
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