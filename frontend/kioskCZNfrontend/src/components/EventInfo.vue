<template>
    <div class="col">
        <div :class="timeEventClass">
            <span v-if="props.eventTimeStart && props.eventTimeEnd">{{ showTime(props.eventTimeStart, props.eventTimeEnd) }}</span>
        </div>
        <div :class="eventNameClass">
            {{ props.eventName }}
        </div>
    </div>
</template>


<script setup>
import { computed } from 'vue'


const showTime = (startTime, endTime) => {
    const formatTime = (time) => {
        // Берем только часы и минуты (первые 5 символов)
        return time.substring(0, 5);
    };
    return `${formatTime(startTime)} - ${formatTime(endTime)}`;
}

// const timeEvent = computed(() => {
//     return `${props.eventDateStart}-${props.eventDateEnd}`
// })

const timeEventClass = computed(() => ({
    'text-orange-9': !props.pastDayStatus,
    'text-grey-4': props.pastDayStatus
}))

const eventNameClass = computed(() => ({
    'text-indigo-8': !props.pastDayStatus,
    'text-grey-4': props.pastDayStatus
}))

const props = defineProps({
    eventName : {
        type: String,
        default: "Наименование мероприятия"
    },

    eventTimeStart: {
        type: String,
    },
    eventTimeEnd: {
        type: String,

    },

    eventDateStart : {
        type: String,
        default: () => {
            const now = new Date()
            const hours = now.getHours().toString().padStart(2, '0')
            const minutes = now.getMinutes().toString().padStart(2, '0')
            return `${hours}:${minutes}`
        }
    },

    eventDateEnd : {
        type: String,
        default: () => {
            const now = new Date()
            now.setHours(now.getHours() + 1) // Добавляем 1 час
            const hours = now.getHours().toString().padStart(2, '0')
            const minutes = now.getMinutes().toString().padStart(2, '0')
            return `${hours}:${minutes}`
        }
    },

    pastDayStatus: {
        type: Boolean,
        default: false
    }
})
</script>