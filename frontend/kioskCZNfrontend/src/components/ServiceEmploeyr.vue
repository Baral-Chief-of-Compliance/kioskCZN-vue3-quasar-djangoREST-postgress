<template>
    <div class="row justify-between q-mb-md">
        <div class="col">{{ props.post }}</div>
        <div class="col">{{ props.name }}</div>
        <cab-btn class="col" :room="props.room" :floor="props.floor" />
    </div>
</template>

<script setup>
import CabBtn from './btns/CabBtn.vue';

const props = defineProps({
    name: {
        type: String,
        default: 'ФИО'
    },
    post: {
        type: String,
        default: 'Должность'
    },

    room: {
        type: Number,
        default: 306
    },

    floor: {
        type: Number,
        default: 3
    }
})

</script>