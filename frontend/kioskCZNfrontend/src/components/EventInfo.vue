<template>
    <div class="col">
        <div :class="timeEventClass">
            {{ timeEvent }}
        </div>
        <div :class="eventNameClass">
            {{ props.eventName }}
        </div>
    </div>
</template>


<script setup>
import { computed } from 'vue'

const timeEvent = computed(() => {
    return `${props.eventDateStart}-${props.eventDateEnd}`
})

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