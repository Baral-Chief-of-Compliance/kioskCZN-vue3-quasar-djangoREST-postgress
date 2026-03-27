<template>
    <div ref="keyboard" class="q-mt-lg q-mx-sm">
        <div
            class="row justify-center q-mb-md"
            v-for="(lr, index) in lettersRows"
            v-bind:key="index"
        >
            <keyboard-btn 
                class="q-mx-sm"
                v-for="(l, i) in lr"
                v-bind:key="i"
                :letter="l"
                v-model="model"
            />

            <keyboard-clean 
                v-if="index === 1"
                v-model="model"
            />
            <keyboard-cancel
                v-if="index === 2"
                v-model="model"
            />
        </div>
        <div class="row justify-center q-mb-lg q-mx-sm">
            <keyboard-space-btn 
                v-model="model"
            />
        </div>
    </div>
</template>

<script setup>
import KeyboardBtn from './KeyboardBtn.vue';
import KeyboardSpaceBtn from './KeyboardSpaceBtn.vue';
import KeyboardCancel from './KeyboardCancel.vue';
import KeyboardClean from './KeyboardClean.vue';

const model = defineModel({ default: '' })

const lettersRows = [
    ['й', 'ц', 'у','к','е','н','г','ш','щ','з','х','ъ'],
    ['ф','ы','в','а','п','р','о','л','д','ж','э'],
    ['я','ч','с','м','и','т','ь','б','ю',]
]
</script>