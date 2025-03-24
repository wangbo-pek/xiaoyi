<template>
    <div class="title-container">
        <div class="title">
            <span>XiaoYi_Blog</span>
        </div>
        <div class="quote">
            <span>「輕薄之態，施之君子，則喪吾德；施之小人，則殺吾身」</span>
        </div>
    </div>
</template>

<script setup lang='ts'>
    defineOptions({
        name: 'HeaderTitleBig',
        inheritAttrs: false
    })
</script>

<style scoped lang='scss'>
    .title-container {
        height: 100%;

        .title {
            height: 45%;
            display: flex;
            align-items: flex-end;
            justify-content: flex-end;
            margin-right: 15px;

            span {
                font-size: 24px;
                font-weight: 250;
            }
        }

        .quote {
            height: 45%;
            margin-top: 10px;
            margin-right: 10px;
            display: flex;
            align-items: flex-start;
            justify-content: flex-end;

            span {
                font-size: 16px;
                font-weight: 750;
            }
        }
    }
</style>