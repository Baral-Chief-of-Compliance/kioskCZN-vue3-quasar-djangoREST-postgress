<template>
    <q-btn
        class="cab-btn q-px-lg q-py-sm"
        size="lg"
        unelevated
        color="orange"
        no-caps
    >
        <span>
            <span v-if="props.showCabinetLabele">каб. </span>
            <b>{{ props.room }}</b>
            <span v-if="props.floor"> этаж <b>{{ props.floor }}</b></span>
        </span>
    </q-btn>
</template>

<script setup>

const props = defineProps({
    room: {
        type: String,
        default: '306'
    },

    floor: {
        type: Number,
        default: 3
    },
    showCabinetLabele: {
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