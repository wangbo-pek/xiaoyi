<template>
    <!-- 当xs、sm时 -->
    <div v-if="display.xs.value || display.sm.value || display.md.value">
        <div>博客名称(xs、sm、md)</div>
        <div>博客导航(xs、sm、md)</div>
    </div>

    <!-- 当sm、lg、xl、xxl -->
    <div v-if="display.lgAndUp.value" class="header-container">
        <div class="title-big"><HeaderTitleBig></HeaderTitleBig></div>
        <div class="nav-big"><HeaderNavBig></HeaderNavBig></div>
        <div class="widget-big"><HeaderWidgetBig></HeaderWidgetBig></div>
    </div>
</template>

<script setup lang='ts'>
    import {useDisplay} from "vuetify";
    import HeaderNavBig from "@/components/Header/header_nav_big/HeaderNavBig.vue";
    import HeaderTitleBig from "@/components/Header/header_title_big/HeaderTitleBig.vue";
    import HeaderWidgetBig from "@/components/Header/header_widget_big/HeaderWidgetBig.vue";

    defineOptions({
        name: 'Header',
        inheritAttrs: false
    })

    const display = useDisplay()
    console.log(display.name.value)

</script>

<style scoped lang='scss'>
    .header-container {
        display: flex;
        justify-content: center;
        align-items: stretch;
        height: 100%;
        width: 100%;


        .title-big {
            width: 32%;
            height: 100%;
        }

        .nav-big {
            width: 35%;
            height: 100%;
        }

        .widget-big {
            width: 33%;
            height: 100%;
        }
    }
</style>