<template>
    <div class="row text-left">
        <div class="col">
            <div class="day-of-week text-indigo">
                {{ props.dayOfWeek }}
            </div>
            <div class="text-blue">
                {{ dateOfEvent }}
            </div>
        </div>
        <event-info
            v-for="(event, index) in props.events"
            v-bind:key="index"
            :event-name="event.event_name"
            :event-date-start="event.event_start_time"
            :event-date-end="event.event_end_time"
        />
    </div>
</template>

<script setup>
import { computed } from 'vue';

import EventInfo from './EventInfo.vue';
import { formatDateToRussian } from 'src/dates/conveterForEvents';

const dateOfEvent = computed(() => {
    return formatDateToRussian(props.date)
})

const props = defineProps({
    dayOfWeek : {
        type: String,
        default: 'Пн'
    },

    date : {
        type: Date,
        default: () => new Date()
    },

    events : {
        type: Array,
        default: () => []
    },

    currentDay: {
        type: Boolean,
        default: false,
    },

    pastDayStatus: {
        type: Boolean,
        default: false,
    }
})

</script>


<style scoped>
    .day-of-week {
        font-size: 24px;
        font-weight: 700;
    }

</style>