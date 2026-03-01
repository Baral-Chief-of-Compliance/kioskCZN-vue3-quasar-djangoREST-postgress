import {
  SUPPORT_NAVIGATOR,
  VACANCIES,
  EVENTS,
  SMART_ASSISTENT,
  GAMES,
  INFO,
  EMPLOYEES,
  MAP,
  INDEX,
  CHOOSE_PC,
  DOCUMENTS,
  MAIN_INFO_PC
} from './pathName.js';


const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/ChoosePersonalCenter.vue'), name: CHOOSE_PC},
      { path: ':pc([a-zA-Z]+)/', component: () => import('pages/IndexPage.vue'), name: INDEX },
      { path: ':pc([a-zA-Z]+)/' + SUPPORT_NAVIGATOR, component: () => import('pages/NavigatorPage.vue'), name: SUPPORT_NAVIGATOR},
      { path: ':pc([a-zA-Z]+)/' + VACANCIES, component: () => import('pages/VacaniesPage.vue'), name: VACANCIES},
      { path: ':pc([a-zA-Z]+)/' + EVENTS, component: () => import('pages/EventsPage.vue'), name: EVENTS},
      { path: ':pc([a-zA-Z]+)/' + SMART_ASSISTENT, component: () => import('pages/SmartAssistentPage.vue'), name: SMART_ASSISTENT},
      { path: ':pc([a-zA-Z]+)/' + GAMES, component: () => import('pages/GamesPage.vue'), name: GAMES},
      { path: ':pc([a-zA-Z]+)/' + INFO, component: () => import('pages/InfoPage.vue'), name: INFO},
      { path: ':pc([a-zA-Z]+)/' + EMPLOYEES, component: () => import('pages/EmployeesPage.vue'), name: EMPLOYEES},
      { 
          path: ':pc([a-zA-Z]+)/' + MAP, 
          component: () => import('pages/MapPage.vue'), 
          name: MAP,
          props: (route) => ({ 
            activeRoomId: Number(route.query.roomId) || 0,
            activeFloor: Number(route.query.floor) || 0})
        },
      { path: ':pc([a-zA-Z]+)/' + INFO +'/' + DOCUMENTS, component: () => import('pages/DocumentsPage.vue'), name: DOCUMENTS},
      { path: ':pc([a-zA-Z]+)/' + INFO +'/' + MAIN_INFO_PC, component: () => import('pages/MainInfoPCPage.vue'), name: MAIN_INFO_PC}
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
