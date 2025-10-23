<template>
    <q-card
        @click="$emit('clickCard')"
        flat
        class="q-mb-sm service-card"
        :style="styleCard"
    >
        <q-card-section>
            <span 
                class="service-card-titel"
                :style="styleTitelCard"
            
            >
                {{ props.titel }}
            </span>
        </q-card-section>
    </q-card>
</template>

<script setup>
import { computed } from 'vue';

const styleCard = computed(() => ({
    border: props.active ? '2px solid #164FA4' : '2px solid white'
}))

const styleTitelCard = computed(() => ({
    color: props.active ? '#164FA4' : '#000000'
}))

const props = defineProps({
    titel: {
        type: String,
        default: 'Наименование услуги'
    },

    active: {
        type: Boolean,
        default: false
    }
})
</script>

<style scoped>
    .service-card{
        border-radius: 10px !important;
    }

    .service-card-titel{
        font-weight: 600;
        font-size: 20px;
    }
</style>