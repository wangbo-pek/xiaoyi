<template>
    <div class="nav-container">
        <v-btn variant="text" class="my-btn">首页</v-btn>
        <v-btn variant="text" class="my-btn">笔记</v-btn>
        <v-btn variant="text" class="my-btn">文章</v-btn>
        <v-btn variant="text" class="my-btn">日记</v-btn>
        <v-btn variant="text" class="my-btn">关于我</v-btn>
    </div>
</template>

<script setup lang='ts'>
    defineOptions({
        name: 'HeaderNavBig',
        inheritAttrs: false
    })
</script>

<style scoped lang='scss'>
    .nav-container {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: space-evenly;

        .my-btn {
            width: 100px;
            font-size: 20px;
            font-weight: 500;
            text-decoration: underline;
            color: #262323;
            margin: 0 10px;
        }
    }
</style>
