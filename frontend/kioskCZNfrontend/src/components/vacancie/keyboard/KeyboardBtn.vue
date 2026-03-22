<template>
    <q-btn
        class="keyboard-btn"
        @click="addLetter"
        :label="props.letter"
    />
</template>

<script setup>
const props = defineProps({
    letter : {
        type: String,
        default: 'a'
    }
})

const model = defineModel('')

const addLetter = () => {
    model.value += props.letter
}

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