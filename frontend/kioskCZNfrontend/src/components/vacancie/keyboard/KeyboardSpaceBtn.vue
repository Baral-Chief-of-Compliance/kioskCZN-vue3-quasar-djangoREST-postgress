<template>
    <q-btn 
        class="keyboard-btn full-width"
        label="Пробел"
        @click="clickSpace"
    />
</template>

<script setup>
const model = defineModel({ default: '' })

const clickSpace = () => {
    model.value += ' '
}
</script>

<style scoped>
    .keyboard-btn{
        border-radius: 10px;
        height: 9.5vh;
        font-size: 3vh;
        font-weight: 700;
        color: var(--q-dark);
    }
</style>