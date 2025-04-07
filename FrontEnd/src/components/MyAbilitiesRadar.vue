<template>
    <v-card class="pa-4" color="transparent" elevation="0" style="position: relative;">
        <div ref="chartRef" style="width: 100%; height: 400px;"></div>
    </v-card>
</template>

<script setup lang="ts">
    import {ref, onMounted} from 'vue'
    import * as echarts from 'echarts'

    defineOptions({name: 'MyAbilitiesRadar', inheritAttrs: false})

    const chartRef = ref<HTMLDivElement | null>(null)

    onMounted(() => {
        if (chartRef.value) {
            const myChart = echarts.init(chartRef.value)

            const option = {
                backgroundColor: 'transparent',
                radar: {
                    center: ['50%', '50%'],
                    radius: 160,
                    indicator: [
                        {name: '市场理解和商业洞察', max: 100},
                        {name: '敏捷开发和项目管理', max: 100},
                        {name: '需求分析和需求管理', max: 100},
                        {name: '编程开发和技术积累', max: 100},
                        {name: '沟通协作和自我管理', max: 100}
                    ],
                    axisName: {color: '#ddd'},
                    splitLine: {lineStyle: {color: ['#444']}},
                    splitArea: {areaStyle: {color: ['rgba(0,0,0,0)', 'rgba(0,0,0,0)']}},
                    axisLine: {lineStyle: {color: '#333'}}
                },
                series: [
                    {
                        type: 'radar',
                        data: [
                            {
                                value: [60, 70, 80, 55, 60],
                                itemStyle: {color: '#f2cc0f'}
                            }
                        ],
                        lineStyle: {color: '#f2cc0f', width: 2},
                        emphasis: {lineStyle: {width: 4}}
                    }
                ]
            }

            // 重点：延迟触发 resize，等待父容器布局完成
            setTimeout(() => {
                myChart.resize()
            }, 100)

            myChart.setOption(option)
            window.addEventListener('resize', () => {
                myChart.resize()
            })
        }
    })
</script>

<style scoped lang="scss">

</style>
