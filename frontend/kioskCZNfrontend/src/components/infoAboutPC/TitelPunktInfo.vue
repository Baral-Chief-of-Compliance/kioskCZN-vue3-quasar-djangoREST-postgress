<template>
    <div class="row items-center">
        <q-icon 
            v-if="props.icon !== null"
            :name="props.icon"
            color="indigo"
            size="xl"
        >
        </q-icon>
        <div class="q-ml-md text-h4 text-indigo text-bold">
            {{ props.titel }}
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    titel: {
        type: String,
        default: 'Наименование'
    },

    icon: {
        type: String,
        default: null
    }
})

</script>