<template>
    <q-btn
        @click="clearBtn"
        class="keyboard-btn"
        label="Очистить"
    />
</template>

<script setup>
const model = defineModel({ default: ''})

const clearBtn = () => {
    model.value = ''
}

</script>

<style scoped>
    .keyboard-btn{
        border-radius: 10px;
        width: 20.5vh;
        height: 9.5vh;
        font-size: 3vh;
        font-weight: 700;
    }
</style>