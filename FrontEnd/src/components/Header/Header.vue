<template>
    <!-- 当xs、sm时 -->
    <!--<div v-if="display.xs.value || display.sm.value || display.md.value">-->
    <!--    <div>博客名称(xs、sm、md)</div>-->
    <!--    <div>博客导航(xs、sm、md)</div>-->
    <!--</div>-->

    <!-- 当sm、lg、xl、xxl -->
    <!--<div v-if="display.lgAndUp.value" class="header-container"-->
    <div class="header-container" :class="{'changeBackgroundColor':coverImage.isScrollOverViewport}">
        <div class="title-big">
            <HeaderTitle></HeaderTitle>
        </div>
        <div class="nav-big">
            <HeaderNav></HeaderNav>
        </div>
        <div class="widget-big">
            <HeaderWidget></HeaderWidget>
        </div>
    </div>
</template>

<script setup lang='ts'>
    // import {useDisplay} from "vuetify";
    import HeaderNav from "@/components/Header/HeaderNav.vue";
    import HeaderTitle from "@/components/Header/HeaderTitle.vue";
    import HeaderWidget from "@/components/Header/HeaderWidget.vue";
    import useAppearanceStore from "@/store/appearance.ts";

    defineOptions({
        name: 'Header',
        inheritAttrs: false
    })

    const coverImage = useAppearanceStore()
    // const display = useDisplay()
</script>

<style scoped lang='scss'>
    .header-container {
        display: flex;
        justify-content: center;
        align-items: stretch;
        height: 100%;
        width: 100%;
        background-color: rgba(204, 204, 204, 0.35);

        .title-big {
            width: 35%;
            height: 100%;
            padding-right: 30px;
        }

        .nav-big {
            width: 35%;
            height: 100%;
        }

        .widget-big {
            width: 30%;
            height: 100%;
        }

    }
    .changeBackgroundColor {
            background-color: #17687a;
        }

</style>