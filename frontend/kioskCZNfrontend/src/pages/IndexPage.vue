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
import CardMenu from 'src/components/CardMenu.vue';
import {
  SUPPORT_NAVIGATOR, 
  VACANCIES, 
  EVENTS,
  SMART_ASSISTENT,
  GAMES,
  INFO,
  EMPLOYEES,
  MAP
} from 'src/router/pathName.js';

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
</script>
