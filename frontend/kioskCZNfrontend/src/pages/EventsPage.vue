<template>
    <q-page>
        <titel-page ref="titelEl" titel="Афиша мероприятий" />
        <loading-spinner v-if="loading" :height="loadingHeight" />

        <div v-else class="row">
            <control-weeks-btn @click="weekNumber--" :disable="disableLeftArrow" left />
            <div 
                class="col flex justify-between q-mt-lg" 
                :style="styleTimeTable">
                <div class="row q-mx-xl">
                    <event-day 
                        v-for="(day, index) in weekDays" 
                        v-bind:key="index"
                        :date="day.date"
                        :day-of-week="day.dayOfWeek"
                        :current-day="day.todayStatus"
                        :past-day-status="day.dayPass"
                        :events="eventStore.events"
                    />
                </div>
                
            </div>
            <control-weeks-btn @click="weekNumber++" />
        </div>


    </q-page>
</template>

<script setup>
import { onMounted, onUnmounted, ref, computed, inject, useTemplateRef, watch } from 'vue';

import { useWindowSize, useElementSize } from '@vueuse/core';

import TitelPage from 'src/components/TitelPage.vue';
import { getWeekDates } from 'src/dates/getDatesOfWeek';
import { getNextWeekDate } from 'src/dates/getNextWeek';
import EventDay from 'src/components/EventDay.vue';
import ControlWeeksBtn from 'src/components/btns/ControlWeeksBtn.vue';
import { useEventStore } from 'src/stores/events';
import { getEvents } from 'src/axios/event';
import { usePCStore } from 'src/stores/personalCenter';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';

const loading = ref(true)


const pcStore = usePCStore()
const eventStore = useEventStore()

const {height: windowHeight} = useWindowSize()

const headerHeight = inject('headerHeight')

const loadingHeight = computed(() => {
    return  `${windowHeight.value - headerHeight.value}px`
})

const weekDays = ref([])

// для пролистования недели
const weekNumber = ref(0)

const titelEl = useTemplateRef('titelEl')
const { height: titelPageHeight} = useElementSize(titelEl)

const styleTimeTable = computed(() => ({
    height: `${windowHeight.value - headerHeight.value - titelPageHeight.value - 100}px`
}))

const disableLeftArrow = computed(() => {
    return weekNumber.value > 0 ? false : true
})

function getWeekDateOnPage(){
    const res = getWeekDates(getNextWeekDate(weekNumber.value))
    return res
}


watch(weekNumber, () => {
    weekDays.value = getWeekDateOnPage()
})


const getPCEvents = async() => {
    loading.value = true
    if (pcStore.pcId != null){
        const res = await getEvents(pcStore.pcId)

        if (res.status != 200){
            return;
        }

        eventStore.setStore(res.data)
    }
    loading.value = false
}


let unsubscribePCStoreAction = pcStore.$onAction(
    ({name, after }) => {
        after(async() => {
            if (name === 'setStore'){
                await getPCEvents()
            }
        })
    }
)



onMounted(async() => {
    await getPCEvents()
    weekDays.value = getWeekDateOnPage()
})

onUnmounted(() => {
    if (unsubscribePCStoreAction){
        unsubscribePCStoreAction()
    }
})
</script>