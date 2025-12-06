<template>
    <q-page>
        <titel-page ref="titelEl" titel="Афиша мероприятий" />

        <div class="row">
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
                    />
                </div>
                
            </div>
            <control-weeks-btn @click="weekNumber++" />
        </div>


    </q-page>
</template>

<script setup>
import { onMounted, ref, computed, inject, useTemplateRef, watch } from 'vue';

import { useWindowSize, useElementSize } from '@vueuse/core';

import TitelPage from 'src/components/TitelPage.vue';
import { getWeekDates } from 'src/dates/getDatesOfWeek';
import { getNextWeekDate } from 'src/dates/getNextWeek';
import EventDay from 'src/components/EventDay.vue';
import ControlWeeksBtn from 'src/components/btns/ControlWeeksBtn.vue';


const {height: windowHeight} = useWindowSize()

const headerHeight = inject('headerHeight')

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


onMounted(() => {
    weekDays.value = getWeekDateOnPage()
})
</script>