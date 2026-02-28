<template>
    <div ref="serviceName" :class="className" style="font-weight: 600;">
        {{ props.label }}
    </div>
</template>


<script setup>
import { computed, useTemplateRef, watch } from 'vue';
import { useElementSize } from '@vueuse/core';


const serviceNameEl = useTemplateRef('serviceName')
const { height: serviceNameHeight } = useElementSize(serviceNameEl)

const model = defineModel(0)

const props = defineProps({
    label: {
        type: String,
        default: 'Наименование сервиса'
    },

    forDocument: {
        type: Boolean,
        default: false
    }
})


const className = computed(() => ({
    "text-center": true,
    "text-orange": true,
    "text-h4": !props.forDocument,
    "text-h6": props.forDocument
}))


watch(serviceNameHeight, (newValue) => {
    model.value = newValue
})
</script>