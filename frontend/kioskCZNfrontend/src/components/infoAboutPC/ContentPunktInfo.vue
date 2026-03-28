<template>
    <div class="text-blue text-h5 content-text">
        {{ props.content }}
    </div>
</template>

<script setup>

const props = defineProps({
    content: {
        type: String,
        default: 'Не указан'
    }
})

</script>

<style scoped>

.content-text{
    font-weight: 500;
}
</style>