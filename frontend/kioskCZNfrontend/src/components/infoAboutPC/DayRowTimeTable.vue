<template>
    <div class="row">
        <div class="col text-h5 text-indigo day-of-week">
            {{ defineDayOfWeek }}
        </div>
        <div :class="timeClass">
            {{ defineTime }}
        </div>
    </div>

</template>

<script setup>
import { computed } from 'vue';

const nameOfDaysWeek = {
    0: 'Понедельник',
    1: 'Вторник',
    2: 'Среда',
    3: 'Четверг',
    4: 'Пятница',
    5: 'Суббота',
    6: 'Воскресенье',
}

const defineDayOfWeek = computed(() => {
    return nameOfDaysWeek[props.dayOfWeek]
}) 

const timeClass = computed(() => ({
    'text-h5 time-of-day col' : true,
    'text-blue': !props.dayOff,
    'text-orange': props.dayOff
}))

const defineTime = computed(() => {
    if (!props.dayOff){
        const startTime = props.timeStart.slice(0, -3)
        const endTime = props.timeEnd.slice(0, -3)
        return `${startTime} - ${endTime}`
    }else{
        return 'Выходной'
    }
})

const props = defineProps({
    dayOfWeek: {
        type: Number,
        default: 0
    },

    dayOff: {
        type: Boolean,
        default: false
    },

    timeStart: {
        type: String,
        default: '08:45:00'
    },

    timeEnd: {
        type: String,
        default: '17:00:00'
    }
})

</script>

<style scoped>

.day-of-week{
    font-weight: 500;
}

.time-of-day{
    font-weight: 600;
}
</style>