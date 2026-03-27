<template>
    <q-btn 
        class="keyboard-btn"
        @click="addNumber"
        :label="props.number"
        :disable="disabelBtn"
    />
</template>

<script setup>
import { computed } from 'vue';


const props = defineProps({
    number: {
        type: Number,
        default: 1
    }
})

const model = defineModel({ default: '' })

const addNumber = () => {
    model.value += props.number
}

const disabelBtn = computed(() => {
    if (model.value.length > 0 && model.value[0] === '0'){
        return true
    }else{
        return false
    }

})
</script>

<style scoped>

.keyboard-btn{
    border-radius: 10px;
    width: 9.5vh;
    height: 9.5vh;
    font-size: 3vh;
    font-weight: 700;
}
</style>