<template>
    <div class="content-container">
        <div class="article-list">
            <template v-for="(item, index) in noteStore.noteList" :key="item.noteListId">
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
    import {onMounted, onUnmounted, ref} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";
    import Card from "@/components/Card.vue";

    defineOptions({
        name: 'Note',
        inheritAttrs: false
    })

    const noteStore = useNoteStore()
    const $router = useRouter()
    let appearanceStore = useAppearanceStore()


    // const jumpTo = (noteListId: number) => {
    //     $router.push({
    //         name: 'noteDetail',
    //         params: {
    //             id: noteListId
    //         }
    //     })
    // }

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

    .scale-fade-enter-active,
    .scale-fade-leave-active {
        transition: all 0.3s ease;
    }

    .scale-fade-enter-from {
        transform: scale(0.8);
        opacity: 0;
    }

    .scale-fade-enter-to {
        transform: scale(1);
        opacity: 1;
    }

    .scale-fade-leave-from {
        transform: scale(1);
        opacity: 1;
    }

    .scale-fade-leave-to {
        transform: scale(0.8);
        opacity: 0;
    }

    .card-dialog {
        position: fixed;
        inset: 0;
        background-color: rgba(0, 0, 0, 0.4);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 2000;

        .card-dialog-content {
            width: 600px;
            max-height: 90vh;
            background: white;
            border-radius: 12px;
            padding: 24px;
            overflow: auto;
        }
    }

</style>