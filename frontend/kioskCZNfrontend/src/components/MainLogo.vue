<template>
    <img 
        alt="CZN Logo"
        src="/src/assets/czn-logo.svg"
        :style="{
            width: width + 'px',
            height: height + 'px'
        }"
        class="q-ml-xl"
    >
</template>

<script setup>

defineProps({
    width: {
        type: Number,
        default: 150
    },

    height: {
        type: Number,
        default: 100
    }
})
</script>