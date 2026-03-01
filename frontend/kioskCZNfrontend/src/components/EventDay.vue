<template>
    <div class="col-6">
        <div class="row text-left">
            <div class="col">
                <div 
                    :class="dayOfWeekClass">
                    {{ props.dayOfWeek }}
                </div>

                <div 
                    :class="dayOfEventClass">
                    {{ dateOfEvent }}
                </div>
            </div>
            <div class="col">
                <event-day-empty v-if="emptyDay" />
                <event-info
                    v-else
                    class="q-mb-lg"
                    v-for="(event, index) in props.events.filter(ev => new Date(ev.date_start).toDateString() === new Date(props.date).toDateString())"
                    v-bind:key="index"
                    :event-name="event.name"
                    :event-date-start="event.date_start"
                    :event-date-end="event.date_end"
                    :past-day-status="props.pastDayStatus"
                    :event-time-start="event.time_start"
                    :event-time-end="event.time_end"
                />
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';

import EventInfo from './EventInfo.vue';
import EventDayEmpty from './EventDayEmpty.vue';
import { formatDateToRussian } from 'src/dates/conveterForEvents';

const dateOfEvent = computed(() => {
    return formatDateToRussian(props.date)
})

const emptyDay = computed(() => props.events.filter(ev => new Date(ev.date_start).toDateString() === new Date(props.date).toDateString()).length > 0 ? false : true)

const dayOfWeekClass = computed(() => ({
    'text-h1': true,
    'text-weight-medium': true,
    'text-indigo': !props.pastDayStatus && !props.currentDay,
    'text-grey': props.pastDayStatus,
    'text-orange-9': props.currentDay
}))

const dayOfEventClass = computed(() => ({
    'text-h4': true,
    'text-blue': !props.pastDayStatus && !props.currentDay,
    'text-grey-5': props.pastDayStatus,
    'text-orange-8': props.currentDay
}))

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