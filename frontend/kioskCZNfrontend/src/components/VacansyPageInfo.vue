<template>
    <div class="row text-center text-h5 text-primary">
        <div class="col">
            Кол-во рабочих мест: <span class="text-bold">{{ props.workPlaces }}</span>
        </div>
        <div class="col">
            <span class="text-bold">{{ props.currentPage }} / {{ props.pages }}</span>
        </div>
        <div class="col">
            Кол-во вакансий: <span class="text-bold">{{ props.count }}</span>
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    count: {
        type: Number,
        default: 0,
    },

    workPlaces: {
        type: Number,
        default: 0
    },

    currentPage: {
        type: Number,
        default: 0
    },

    pages: {
        type: Number,
        default: 0
    }
})

</script>