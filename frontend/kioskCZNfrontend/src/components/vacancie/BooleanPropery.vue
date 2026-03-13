<template>
    <q-avatar
        class="q-mb-sm" 
        size="md"
        text-color="white"
        rounded
        :color="color"
        :icon="icon"
    />
</template>

<script setup>
import { computed } from 'vue';

const color = computed(() => {
    return props.value? 'indigo-9' : 'grey-6'
})

const icon = computed(() => {
    return props.value? 'check' : 'close'
})

const props = defineProps({
    value: {
        type: Boolean
    }
})
</script>