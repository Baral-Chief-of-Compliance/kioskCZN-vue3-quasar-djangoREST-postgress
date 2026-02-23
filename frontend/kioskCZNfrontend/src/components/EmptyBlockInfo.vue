<template>
    <div class="flex flex-center" :style="{
        height: props.height
    }">
        <div class="q-gutter-md row items-center">
        <span class="text-h5 text-center text-primary text-bold">{{ props.text }}</span>
        </div>
  </div>
</template>

<script setup>

const props = defineProps({
    text: {
        type: String,
        default: 'Ой, к сожалению тут ничего нет...'
    },
    height:{
        type: String,
        default: '400px'
    }
})
</script>