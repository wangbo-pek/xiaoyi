<template>
    <div class="home-container">

        <div class="recommended-container">
            <div class="recommended-tab">
                推荐文章
            </div>
            <div class="recommended-list">
                <template v-for="item in noteStore.recommendedNoteList" :key="item">
                    <Card
                        :title="item.title"
                        :bgImage="item.coverImg"
                        :createdDate="item.createdTime"
                        :category="item.category"
                        :tags="item.tagsName"
                    ></Card>
                </template>
            </div>
        </div>

        <div class="random-note-container">
            <div class="random-note-tab">
                最新文章
            </div>
            <div class="random-note-list">
                <template v-for="item in noteStore.latestNoteList" :key="item">
                    <Card
                        :title="item.title"
                        :bgImage="item.coverImg"
                        :createdDate="item.createdTime"
                        :category="item.category"
                        :tags="item.tagsName"
                    ></Card>
                </template>
            </div>
        </div>

    </div>
</template>

<script setup lang='ts'>
    import useNoteStore from "@/store/note.ts";
    import Card from "@/components/Card.vue";
    import {watch} from "vue";

    defineOptions({
        name: 'Home',
        inheritAttrs: false
    })

    const noteStore = useNoteStore()

    // 监听App.vue是否拿到了NoteList，如果拿到了，就获取被置顶的文章、最新的文章
    watch(() => noteStore.noteList, () => {
        // 获取被置顶的文章
        noteStore.recommendedNoteList = noteStore.noteList.filter((value) => {
            return value.isRecommended === true
        })

        // 获取最新的文章
        noteStore.latestNoteList = noteStore.noteList.slice(0, 4)
    })

</script>

<style scoped lang='scss'>
    .home-container {
        height: 100%;
        border-radius: 5px;
        padding: 2px 10px;

        .recommended-container {
            background-color: rgba(3, 27, 31, 0.5);
            padding: 50px;
            margin: 25px;
            border-radius: 20px;

            .recommended-tab {
                color: white;
                text-align: center;
                font-size: 25px;
                font-weight: 800;
                margin-bottom: 30px;
            }

            .recommended-list {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
                column-gap: 3px;
                row-gap: 20px;
                padding: 10px 20px 20px 30px;
                justify-items: center;
            }
        }

        .random-note-container {
            background-color: rgba(3, 27, 31, 0.5);
            padding: 50px;
            margin: 25px;
            border-radius: 20px;

            .random-note-tab {
                color: white;
                text-align: center;
                font-size: 25px;
                font-weight: 800;
                margin-bottom: 30px;
            }

            .random-note-list {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
                column-gap: 3px;
                row-gap: 20px;
                padding: 10px 20px 20px 30px;
                justify-items: center;
            }
        }
    }

</style>