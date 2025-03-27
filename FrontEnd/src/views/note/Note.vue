<template>
    <div class="content-container">
        <div class="article-list">
            <template v-for="item in noteStore.noteList" :key="item.noteListId">
                <Card
                    :title="item.title"
                    :subtitle="item.subtitle"
                    :bgImage="item.coverImg"
                    :createdDate="item.createdTime"
                    :secondClassification="item.secondClassification"
                    :tags="item.tagsName"
                ></Card>
            </template>
        </div>
    </div>

</template>

<script setup lang='ts'>
    import useNoteStore from "@/store/note.ts";
    import {useRouter} from "vue-router";
    import {onMounted, onUnmounted} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";
    import Card from "@/components/Card.vue";

    defineOptions({
        name: 'Note',
        inheritAttrs: false
    })

    const noteStore = useNoteStore()
    const $router = useRouter()
    let appearanceStore = useAppearanceStore()

    const jumpTo = (noteListId: number) => {
        $router.push({
            name: 'noteDetail',
            params: {
                id: noteListId
            }
        })
    }

    onMounted(() => {
        appearanceStore.isShowHomeCover = false
        appearanceStore.isScrollOverViewport = true
    })

    onUnmounted(() => {
        appearanceStore.isShowHomeCover = true
    })
</script>

<style scoped lang="scss">
    .content-container {
        position: relative;
        width: 100%;
        height: 100%;

        .article-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            column-gap: 34px;
            row-gap: 40px;
            padding: 80px 20px 30px 20px;
            justify-items: center;
        }
    }

</style>