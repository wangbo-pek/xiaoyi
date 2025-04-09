<template>
    <div class="tag-container">
        <div class="my-category-title">
            ——&nbsp;&nbsp;&nbsp;文章分类&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-category-container">
            <div class="categories-chip">
                <template v-for="item in categoriesStore.categoryStats" :key="item.category">
                    <MyChip
                        :name="item.category"
                        :noteCount="item.note_count"
                        :color="item.color"
                    ></MyChip>
                </template>
            </div>

            <!-- 柱状图 -->
            <div class="categoryChartRef" ref="categoryChartRef"></div>
        </div>

        <div class="my-tag-title">
            ——&nbsp;&nbsp;&nbsp;文章标签&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-tag-container">
            <div class="tags-chip">
                <template v-for="item in tagsStore.tagStats" :key="item.tag">
                    <MyChip
                        :name="item.tag"
                        :noteCount="item.tag_count"
                        :color="item.color"
                    ></MyChip>
                </template>
            </div>

            <!-- 词云在这里展示 -->
            <div class="tagWordCloudRef" ref="tagWordCloudRef"></div>
        </div>
    </div>
    <div class="placeholder"></div>
</template>

<script setup lang='ts'>
    import {nextTick, onMounted, onUnmounted, ref} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";
    import useCategoriesStore from "@/store/categories.ts";
    import useTagsStore from "@/store/tags.ts";
    import axios_server from "@/utils/axios_server.ts";
    import * as echarts from 'echarts'
    import 'echarts-wordcloud'
    import MyChip from "@/components/MyChip.vue";

    defineOptions({
        name: 'Tag',
        inheritAttrs: false
    })

    let appearanceStore = useAppearanceStore()
    let categoriesStore = useCategoriesStore()
    let tagsStore = useTagsStore()

    const bgColor = [
        'rgba(196,86,62,0.8)',
        'rgba(125,150,46,0.8)',
        'rgba(54,169,104,0.8)',
        'rgba(59,110,161,0.8)',
        'rgba(215,96,163,0.8)',
        'rgba(150,96,215,0.8)',
        'rgba(89,182,63,0.8)',
        'rgba(206,191,93,0.8)',
    ]

    const categoryChartRef = ref<HTMLDivElement | null>(null)
    let categoryChart: echarts.ECharts | null = null
    const tagWordCloudRef = ref<HTMLDivElement | null>(null)
    let tagChart: echarts.ECharts | null = null

    const initCategoryChart = () => {
        if (!categoryChartRef.value) return

        const xData = categoriesStore.categoryStats.map(item => item.category)
        const seriesData = categoriesStore.categoryStats.map((item) => ({
            value: item.note_count,
            itemStyle: {
                color: item.color
            }
        }))

        categoryChart = echarts.init(categoryChartRef.value)

        categoryChart.setOption({
            xAxis: {
                type: 'category',
                data: xData
            },
            yAxis: {
                type: 'value'
            },
            series: [{
                type: 'bar',
                data: seriesData
            }]
        })

        categoryChart.resize()
    }
    const initTagWordCloud = () => {
        if (!tagWordCloudRef.value) return

        const data = tagsStore.tagStats.map((tag: any) => ({
            name: tag.tag,
            value: tag.tag_count,
            textStyle: {
                color: tag.color
            }
        }))

        tagChart = echarts.init(tagWordCloudRef.value)
        tagChart.setOption({
            series: [{
                type: 'wordCloud',
                shape: 'circle',
                sizeRange: [12, 40],
                rotationRange: [-90, 90],
                gridSize: 8,
                textStyle: {
                    fontFamily: 'sans-serif'
                },
                data: data
            }]
        })

        tagChart.resize()
    }

    onMounted(() => {
        appearanceStore.isShowHomeCover = false
        appearanceStore.isScrollOverViewport = true

        axios_server.get('getAllCategoryCount/').then(
            async (response) => {
                const categoriesRaw = response.data
                categoriesStore.categoryStats = categoriesRaw.map((item: any, index: any) => ({
                    ...item,
                    color: bgColor[index % bgColor.length]
                }))
                await nextTick()
                initCategoryChart()
            }
        ).catch(err => {
            console.error('获取分类出错', err)
        })

        axios_server.get('getAllTagCount/').then(
            async (response) => {
                tagsStore.tagStats = response.data
                tagsStore.tagStats.forEach((value) => {
                    value.color = bgColor[Math.floor(Math.random() * 7)]
                })
                await nextTick()
                initTagWordCloud()
            }
        ).catch(err => {
            console.error('获取标签出错', err)
        })

    })

    onUnmounted(() => {
        appearanceStore.isShowHomeCover = true

        if (categoryChart) {
            categoryChart.dispose()
            categoryChart = null
        }
    })
</script>

<style scoped lang="scss">
    .tag-container {
        position: relative;
        top: 1rem;

        .my-category-title {
            margin: 100px 0 30px 250px;
            text-align: left;
            color: white;
            font-size: 1.5rem;
        }

        .my-category-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            position: relative;
            left: 12rem;

            .categories-chip {
                position: relative;
                left: 3rem;
            }

            .categoryChartRef {
                width: 85%;
                height: 350px;
            }
        }

        .my-tag-title {
            margin: 10px 0 30px 250px;
            text-align: left;
            color: white;
            font-size: 1.5rem;
        }

        .my-tag-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            position: relative;
            left: 12rem;

            .tags-chip {
                position: relative;
                left: 3rem;
            }

            .tagWordCloudRef {
                background-color: rgba(255, 255, 255, 0.05);
                width: 70%;
                height: 400px;
                margin-top: 10px;
                margin-left: 60px;
            }
        }
    }

    .placeholder {
        margin-bottom: 50px;
    }
</style>