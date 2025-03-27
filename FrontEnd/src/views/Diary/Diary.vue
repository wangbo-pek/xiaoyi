<template>
<div>diary</div>
</template>

<script setup lang='ts'>
    defineOptions({
        name: 'Diary',
        inheritAttrs: false
    })

    import {onMounted, onUnmounted} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";

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