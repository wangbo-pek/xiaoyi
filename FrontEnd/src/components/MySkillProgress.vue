<template>
    <div class="skill-item">
        <div class="skill-name">
            {{ name }}
            <span class="skill-value">{{ level }}%</span>
        </div>
        <div class="progress-bar">
            <div
                class="progress-fill"
                :style="{ width: level + '%' }"
            ></div>
        </div>
    </div>
</template>

<script setup lang='ts'>
    defineOptions({
        name: 'MySkillProgress',
        inheritAttrs: false
    })

    defineProps<{
        name: string
        level: number
    }>()
</script>

<style scoped lang='scss'>
    .skill-item {
        margin-bottom: 16px;

        .skill-name {
            display: flex;
            justify-content: space-between;
            font-size: 15px;
            font-weight: 500;
            color: #fff;
            margin-bottom: 4px;
        }

        .progress-bar {
            width: 100%;
            height: 25px;
            background-color: rgba(68, 68, 68, 0.25);
            border-radius: 5px;
            overflow: hidden;

            .progress-fill {
                height: 100%;
                background: linear-gradient(90deg, #ff9800, #ffc107);
                transition: width 0.8s ease;
                border-radius: 6px;
            }
        }
    }
</style>