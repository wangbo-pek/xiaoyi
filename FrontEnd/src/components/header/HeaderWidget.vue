<template>
    <div class="widget-container">

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