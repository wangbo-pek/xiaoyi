<template>
    <div class="main" ref="mainContentRef">
        <div class="content">
            <div>
                <div>first</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
                <div>home</div>
            </div>
        </div>
    </div>

</template>

<script setup lang='ts'>

    defineOptions({
        name: 'Home',
        inheritAttrs: false
    })

</script>

<style scoped lang='scss'>
    .headerbar {
        padding: 0;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 5vh;
        z-index: 1000;
    }

    .main {
        width: 100%;
        min-height: 90vh;
        display: flex;
        justify-content: right;
        align-items: flex-start;
        gap: 10px;
        z-index: 900;

        .content {
            flex: 0 0 75%;
            height: 100%;
            border-radius: 5px;
            padding: 2px 10px;
            position: relative;
            left: -50px
        }

        .siderbar {
            background-color: lightblue;
            flex: 0 0 15%;
            height: 100%;
            border-radius: 5px;
            padding: 10px;
            overflow-y: auto;
            position: relative;
            left: -5px
        }
    }
</style>