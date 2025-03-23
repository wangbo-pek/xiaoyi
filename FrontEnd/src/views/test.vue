<template>
    <div>
        <p class="test">我是test</p>
        <v-btn @click="test1">我是vuetify的btn1</v-btn>
        <v-btn @click="test2">我是vuetify的btn2</v-btn>
    </div>
</template>

<script setup lang='ts'>
    import axios from "axios";
    import axios_server from "../utils/axios_server.ts";

    defineOptions({
        name: 'Test',
        inheritAttrs: false
    })

    const test1 = () => {
        axios.get('http://127.0.0.1:8000/test/', {data: 'get test'}).then((response) => {
            console.log(response)
        })
        console.log(document.cookie)
    }

    const test2 = () => {
        axios_server.post('http://localhost:8000/test/', {data: 'post test'}).then((response) => {
            console.log(response)
        })
    }

</script>

<style scoped lang="scss">
    @import "@/styles/_variables.scss";

    .test {
        color:$test-color;
    }
</style>