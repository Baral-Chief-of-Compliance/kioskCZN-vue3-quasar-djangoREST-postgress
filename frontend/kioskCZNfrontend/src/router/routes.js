import {
  SUPPORT_NAVIGATOR,
  VACANCIES,
  EVENTS,
  SMART_ASSISTENT,
  GAMES,
  INFO,
  EMPLOYEES,
  MAP
} from './pathName.js';


const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue'), name: 'index'},
      { path: SUPPORT_NAVIGATOR, component: () => import('pages/NavigatorPage.vue'), name: SUPPORT_NAVIGATOR},
      { path: VACANCIES, component: () => import('pages/VacaniesPage.vue'), name: VACANCIES},
      { path: EVENTS, component: () => import('pages/EventsPage.vue'), name: EVENTS},
      { path: SMART_ASSISTENT, component: () => import('pages/SmartAssistentPage.vue'), name: SMART_ASSISTENT},
      { path: GAMES, component: () => import('pages/GamesPage.vue'), name: GAMES},
      { path: INFO, component: () => import('pages/InfoPage.vue'), name: INFO},
      { path: EMPLOYEES, component: () => import('pages/EmployeesPage.vue'), name: EMPLOYEES},
      { path: MAP, component: () => import('pages/MapPage.vue'), name: MAP},

      
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
]

export default routes
