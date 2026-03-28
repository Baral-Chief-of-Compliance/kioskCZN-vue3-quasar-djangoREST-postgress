<template>
    <div class="text-left text-h3 text-indigo text-bold tab-titel">
        {{ props.titelFirst }}<br>{{ props.titelSecond }}
    </div>
</template>

<script setup>

const props = defineProps({
    titelFirst: {
        type: String,
        default: 'Наименование панели'
    },

    titelSecond: {
        type: String,
        default: ''
    }
})
</script>

<style scoped>


</style>