<template>
    <q-btn
        class="cab-btn q-px-lg q-py-sm"
        size="lg"
        unelevated
        color="orange"
        no-caps
    >
        <span>каб. <b>{{ props.room }}</b> этаж <b>{{ props.floor }}</b></span>
    </q-btn>
</template>

<script setup>

const props = defineProps({
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

<style scoped>
    .cab-btn{
        border-radius: 10px !important;
    }
</style>