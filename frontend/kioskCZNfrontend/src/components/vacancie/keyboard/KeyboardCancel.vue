<template>
    <q-btn
        class="keyboard-btn"
        @click="eraseLetter"
        icon="backspace"
    />
</template>

<script setup>
const model = defineModel({ default: '' })

const eraseLetter = () => {
    if (model.value.length > 0){
        model.value = model.value.slice(0, model.value.length - 1)
    }
}

</script>

<style scoped>
.keyboard-btn{
    border-radius: 10px;
    width: 9.5vh;
    height: 9.5vh;
    font-size: 3vh;
    font-weight: 700;
    color: var(--q-dark);
}

</style>