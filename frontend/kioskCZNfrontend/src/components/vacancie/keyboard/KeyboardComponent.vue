<template>
    <div ref="keyboard" class="q-mt-lg q-mx-sm">
        <div
            class="row flex justify-center content-center q-mb-md"
            v-for="(lr, index) in lettersRows"
            v-bind:key="index"
        >
            <keyboard-btn 
                class="q-mx-sm"
                v-for="(l, i) in lr"
                v-bind:key="i"
                :letter="l"
            />
        </div>
    </div>
</template>

<script setup>
import KeyboardBtn from './KeyboardBtn.vue';

const lettersRows = [
    ['й', 'ц', 'у','к','е','н','г','ш','щ','з','х','ъ'],
    ['ф','ы','в','а','п','р','о','л','д','ж','э'],
    ['я','ч','с','м','и','т','ь','б','ю',]
]
</script>