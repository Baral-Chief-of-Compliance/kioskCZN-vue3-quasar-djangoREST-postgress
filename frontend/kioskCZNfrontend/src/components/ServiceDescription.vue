<template>
    <div v-html="props.rawHtml">
    </div>
</template>

<script setup>
    const props = defineProps({
        rawHtml: {
            type: String
        }
    })
</script>

<style scoped>
    h1{
        font-size: 20px !important;
    }
</style>