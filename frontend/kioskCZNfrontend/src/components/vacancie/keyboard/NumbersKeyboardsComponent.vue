<template>
    <div>
        <div class="row justify-center q-mb-md"
            v-for="(nr, index) in numbersRows"
            v-bind:key="index"
        >
            <keyboard-number-btn 
                class="q-mx-sm"
                v-for="(n, i) in nr"
                v-bind:key="i"
                :number="n"
                v-model="model"
            />
        </div>
    </div>
</template>

<script setup>
import KeyboardNumberBtn from './KeyboardNumberBtn.vue';


const model = defineModel({default: ''})

const numbersRows = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
</script>