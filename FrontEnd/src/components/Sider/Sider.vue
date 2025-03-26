<template>
    <div class="sider-container">
        <div class="something">
            <v-icon>mdi-home</v-icon>
        </div>
    </div>
</template>

<script setup lang='ts'>
    defineOptions({
        name: 'Sider',
        inheritAttrs: false
    })
</script>

<style scoped lang='scss'>
    .sider-container {
        position: relative;
        width: 100%;
        height: 100%;

        .something {
            position: relative;
            top: 8vh;
            width: 100%;
        }
    }
</style>