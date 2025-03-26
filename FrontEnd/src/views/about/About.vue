<template>
    <div>about me</div>
</template>

<script setup lang='ts'>
    import {onMounted, onUnmounted} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";

    defineOptions({
        name: 'About',
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

</style>