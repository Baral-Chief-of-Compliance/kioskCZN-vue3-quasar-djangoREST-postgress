<template>
    <q-btn :disable="props.disable" flat class="q-mt-lg" color="blue" style="width: 100px">
        <template:icon v-if="!props.disable">
            <q-icon 
                :name="defineArrowDirection" 
                size="20rem" />
        </template:icon>
    </q-btn>
</template>

<script setup>
import { computed } from 'vue';

const defineArrowDirection = computed(() => {
    return props.left? 'arrow_left' : 'arrow_right' 
})

const props = defineProps({
    left: {
        type: Boolean,
        default: false
    },

    disable: {
        type: Boolean,
        default: false
    }
})
</script>

