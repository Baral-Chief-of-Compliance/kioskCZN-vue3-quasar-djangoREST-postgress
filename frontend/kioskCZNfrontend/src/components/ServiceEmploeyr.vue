<template>
    <div class="row justify-between q-mb-md">
        <div class="col q-mr-xl">{{ props.post }}</div>
        <div class="col q-mr-xl">{{ props.name }}</div>
        <cab-btn 
            class="col"
            :room="props.room"
            :floor="props.floor" 
            :disable="props.disableCabBtn"
        />
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
        type: String,
        default: '306'
    },

    floor: {
        type: Number,
        default: 3
    },

    disableCabBtn:{
        type: Boolean,
        default: false
    }
})

</script>