<template>
    <div class="sider-container">
        <div class="introduction">
            <div class="my-avatar">
                <v-icon class="my-avatar-icon">mdi-home</v-icon>
            </div>
            <div class="my-name">
                <span class="my-name-text">Wang</span>
            </div>
            <div class="what-i-wanna-say">
                <span class="what-i-wanna-say-text">人的一生就应该像一条河，开始是涓涓细流，被狭窄的河岸所束缚，然后，它激烈地奔过巨石，冲越瀑布。渐渐地，河流变宽了，两边的堤岸也远去，河水流动得更加平静。最后，它自然地融入了大海，并毫无痛苦地消失了自我。</span>
            </div>
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
        display: flex;
        justify-content: center; /* 水平居中 */

        .introduction {
            text-align: center; /* 如果需要，确保文本水平居中 */
            position: relative;
            top: 5rem;
            width: 100%;
        }
    }
</style>