<template>
    <v-app>
        <canvas id="stars"></canvas>
        <div class="bg-overlay"></div>
        <router-view></router-view>
    </v-app>
</template>

<script setup lang='ts'>
    import {onMounted} from "vue";
    import useNoteStore from "@/store/note.ts";
    import useDiaryStore from "@/store/diary.ts";
    import axios_server from "./utils/axios_server.ts";

    defineOptions({
        name: 'App',
        inheritAttrs: false
    })

    let noteStore = useNoteStore()
    let diaryStore = useDiaryStore()

    onMounted(() => {
        // 每次App.vue加载，都会发送请求，设置csrf_token
        axios_server.get('csrf/').then(() => {
            // 每次App.vue加载，都会发送请求，获取Note文章列表信息
            axios_server.get('getAllNoteList/').then(
                (response) => {
                    // 把文章列表信息保存到noteStore仓库中
                    noteStore.noteList = response.data
                    console.log('>>>> noteStore.noteList <<<<')
                    console.log(noteStore.noteList)
                }
            )
            axios_server.get('getAllDiaryList/').then(
                (response) => {
                    // 把文章列表信息保存到diaryStore仓库中
                    diaryStore.diaryList = response.data
                    diaryStore.diaryList.forEach((value) => {
                        value.timelinePointColor = diaryStore.timelinePointColor[Math.floor(Math.random() * diaryStore.timelinePointColor.length)]
                    })
                    console.log('>>>> diaryStore.diaryList <<<<')
                    console.log(diaryStore.diaryList)
                }
            )

            const canvas = document.getElementById("stars") as HTMLCanvasElement;
            const ctx = canvas.getContext("2d")!;
            const stars: { x: number, y: number, r: number, vx: number, vy: number }[] = [];
            const STAR_COUNT = 20;

            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            for (let i = 0; i < STAR_COUNT; i++) {
                stars.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    r: Math.random() * 2 + 1,
                    vx: (Math.random() - 0.5) * 0.5,
                    vy: (Math.random() - 0.5) * 0.5
                });
            }

            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                stars.forEach(s => {
                    ctx.beginPath();
                    ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                    ctx.fillStyle = "white";
                    ctx.shadowColor = "white";         // ⭐ 添加这一行
                    ctx.shadowBlur = s.r * 4;          // ⭐ 发光强度随星星大小
                    ctx.fill();
                    s.x += s.vx;
                    s.y += s.vy;
                    if (s.x < 0 || s.x > canvas.width) s.vx *= -1;
                    if (s.y < 0 || s.y > canvas.height) s.vy *= -1;
                });
                requestAnimationFrame(draw);
            }

            draw();
        })
    })
</script>

<style lang="scss">
    #stars {
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        background: black;
        opacity: 1;
    }

    .bg-overlay {
        position: fixed;
        inset: 0;
        z-index: 0;
        background: radial-gradient(ellipse at center,
            rgba(17, 60, 70, 0.1) 0%,
            rgba(17, 60, 70, 0.2) 25%,
            rgba(17, 60, 70, 0.3) 50%,
            rgba(17, 60, 70, 0.4) 75%,
            rgba(17, 60, 70, 0.5) 100%);
        pointer-events: none;
    }
</style>