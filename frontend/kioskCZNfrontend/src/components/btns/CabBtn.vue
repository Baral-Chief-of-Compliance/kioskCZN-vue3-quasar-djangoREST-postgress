<template>
    <q-btn
        class="cab-btn q-px-lg q-py-sm"
        size="lg"
        unelevated
        color="orange"
        no-caps
        :disable="props.disable"
        @click="goRoomFloor"
    >
        <span>
            <span v-if="props.showCabinetLabele">каб. </span>
            <b>{{ props.room }}</b>
            <span v-if="props.floor"> этаж <b>{{ props.floor }}</b></span>
        </span>
    </q-btn>
</template>

<script setup>
import { useRouter } from 'vue-router';
import {MAP} from 'src/router/pathName.js';


const router = useRouter()

const goRoomFloor = () => {
    if (!props.disable && props.roomId && props.floor){
        router.push({
            name: MAP,
            query: {
                roomId: props.roomId,
                floor: props.floor
            }
        }) 
    }
}

const props = defineProps({
    room: {
        type: String,
        default: '306'
    },

    roomId: {
        type: Number,
        default: 1
    },

    floor: {
        type: Number,
        default: 3
    },
    showCabinetLabele: {
        type: Boolean,
        default: false
    },

    disable:{
        type: Boolean,
        default: false
    }
})

</script>

<style scoped>
    .cab-btn{
        border-radius: 10px !important;
    }
</style>