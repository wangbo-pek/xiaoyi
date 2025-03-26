<template>
    <div class="widget-container">
        <!--<div class="widget-weather">天气挂件</div>-->
        <!--<div class="widget-date">今日日期</div>-->
        <!--<div class="widget-func">coffee me</div>-->
    </div>
</template>

<script setup lang='ts'>
    defineOptions({
        name: 'HeaderWidget',
        inheritAttrs: false
    })
</script>

<style scoped lang='scss'>
    .widget-container {
        height: 100%;
        display: flex;
        padding: 5px;

        .widget-weather {
            width: 40%;
        }

        .widget-date {
            width: 40%;
        }

        .widget-func {
            width: 20%;
        }
    }
</style>