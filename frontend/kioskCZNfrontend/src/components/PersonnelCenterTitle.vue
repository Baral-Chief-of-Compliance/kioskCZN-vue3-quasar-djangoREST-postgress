<template>
    <div class="pc-titel text-indigo">
        {{ title }}
    </div>
</template>

<script setup>

defineProps({
    title: {
        type: String,
        default: "Наименование Кадрового Центра"
    }
})

</script>

<style scoped>
    .pc-titel{
        font-weight: 700;
        font-size: 40px;
    }
</style>