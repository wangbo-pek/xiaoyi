<template>
    <span
        class="chip"
        :style="{backgroundColor:`${color}`}"
    >
        {{ name }}&nbsp;({{ noteCount }})
    </span>
</template>

<script setup lang='ts'>
    defineOptions({
        name: 'MyChip',
        inheritAttrs: false
    })

    defineProps<{
        name: string
        noteCount: string
        color:string
    }>()

</script>

<style scoped lang='scss'>
    .chip {
        background-color: rgb(255, 255, 0);
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 800;
        color: white;
        line-height: 2rem;
        text-align: center;
        padding: 2px 10px;
        margin: 5px 5px;
    }
</style>