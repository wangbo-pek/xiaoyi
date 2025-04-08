<template>
    <div class="typewriter">
        <span class="text">{{ displayedText }}</span><span class="cursor"></span>
    </div>
</template>

<script setup lang='ts'>
    import {watch, onMounted, ref} from "vue";
    import type {TypingWriter} from "@/store/types/Writer.ts";

    defineOptions({
        name: 'TypeWriter',
        inheritAttrs: false
    })

    const props = defineProps<TypingWriter>()
    const displayedText = ref('')
    const isDeleting = ref(false)
    let timeoutId: ReturnType<typeof setTimeout> | null = null

    onMounted(() => {
        startTyping()
    })

    watch(() => props.text, () => {
        reset()
        startTyping()
    })

    function reset() {
        displayedText.value = ''
        isDeleting.value = false
        if (timeoutId) {
            clearTimeout(timeoutId)
            timeoutId = null
        }
    }

    function startTyping() {
        let i = 0

        const type = () => {
            const fullText = props.text
            const typingSpeed = props.typingSpeed ?? 100
            const deletingSpeed = props.deletingSpeed ?? 50
            const pauseTime = props.pauseTime ?? 1500

            if (!isDeleting.value) {
                displayedText.value = fullText.slice(0, i++)
                if (i > fullText.length) {
                    isDeleting.value = true
                    timeoutId = setTimeout(type, pauseTime)
                    return
                }
            } else {
                displayedText.value = fullText.slice(0, i--)
                if (i < 0) {
                    isDeleting.value = false
                    i = 0
                    timeoutId = setTimeout(type, pauseTime)
                    return
                }
            }
            timeoutId = setTimeout(type, isDeleting.value ? deletingSpeed : typingSpeed)
        }
        type()
    }

</script>

<style scoped lang='scss'>
    .typewriter {
        font-weight: 800;
        font-size: 1.25rem;
        color: white;
        white-space: normal;
        word-break: break-word;
        display: inline;
    }

    .cursor {
        display: inline-block;
        width: 2px;
        height: 1.25rem;
        background-color: white;
        margin-left: 2px;
        animation: blink 1s steps(2, start) infinite;
    }

    @keyframes blink {
        0%, 100% {
            opacity: 1
        }
        50% {
            opacity: 0
        }
    }
</style>