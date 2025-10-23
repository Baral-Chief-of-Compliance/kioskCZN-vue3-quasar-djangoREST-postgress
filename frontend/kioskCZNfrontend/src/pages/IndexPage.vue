<template>
  <q-page class="flex flex-center">
    <div class="row justify-between q-mx-md">
      <card-menu 
      v-for="mp in menuPoints" 
      :key="mp.titel"
      :titel="mp.titel"
      :icon="mp.icon"
      :link="mp.link"
      />
    </div>
  </q-page>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import { getPersonalCenterData } from 'src/axios/personalCenter';
import CardMenu from 'src/components/CardMenu.vue';
import {
  SUPPORT_NAVIGATOR, 
  VACANCIES, 
  EVENTS,
  SMART_ASSISTENT,
  GAMES,
  INFO,
  EMPLOYEES,
  MAP,
  CHOOSE_PC
} from 'src/router/pathName.js';
import { usePCStore } from 'src/stores/personalCenter';
import { useDepartments } from 'src/stores/departments';
import { useDocuments } from 'src/stores/documents';
import { useEventStore } from 'src/stores/events';
import { useFloorsStore } from 'src/stores/floors';
import { useServicesStore } from 'src/stores/services';


const route = useRoute()
const router = useRouter()

const pcStore = usePCStore()
const departmentsStore = useDepartments()
const documentsStore = useDocuments()
const eventsStore = useEventStore()
const floorStore = useFloorsStore()
const servicesStore = useServicesStore()

const menuPoints = [
  {
    titel: 'Навигатор мер поддержки',
    icon: 'assignment',
    link: SUPPORT_NAVIGATOR
  },
  {
    titel: 'Вакансии',
    icon: 'engineering',
    link: VACANCIES
  },
  {
    titel: 'Афиша мероприятий',
    icon: 'calendar_month',
    link: EVENTS
  },
  {
    titel: 'СМАРТ-ассистенты',
    icon: 'smart_toy',
    link: SMART_ASSISTENT
  },
  {
    titel: 'Игры',
    icon: 'sports_esports',
    link: GAMES
  },
  {
    titel: 'Важная информация',
    icon: 'info',
    link: INFO
  },
  {
    titel: 'Сотрудники',
    icon: 'groups',
    link: EMPLOYEES
  },
  {
    titel: 'Карта здания',
    icon: 'map',
    link: MAP
  },
]

onMounted(async() => {
  try{
    const res = await getPersonalCenterData(route.params.pc)
    pcStore.setStore(res)
    departmentsStore.setStore(res)
    documentsStore.setStore(res)
    eventsStore.setStore(res)
    floorStore.setStore(res)
    servicesStore.setStore(res)
  } catch(err){
    console.error(err)
    router.push({name: CHOOSE_PC})
  }
})
</script>
