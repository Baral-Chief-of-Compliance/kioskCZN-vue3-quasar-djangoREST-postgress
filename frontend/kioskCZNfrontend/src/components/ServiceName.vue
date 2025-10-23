<template>
    <div class="text-center text-h4 text-orange" style="font-weight: 600;">
        {{ props.label }}
    </div>
</template>


<script setup>

const props = defineProps({
    label: {
        type: String,
        default: 'Наименование сервиса'
    }
})

</script>