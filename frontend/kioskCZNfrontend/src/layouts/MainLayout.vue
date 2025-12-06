<template>
  <q-layout view="lHh Lpr lFf">
    <q-header ref="headerEl" class="bg-white" elevated>
      <q-toolbar class="row justify-between">
        <q-toolbar-title class="col-2">
            <main-logo />
        </q-toolbar-title>
        <personnel-center-title class="col-8 text-center" />
        <current-date-time class="col-2" />
      </q-toolbar>
    </q-header>
    <q-page-container class="main-page-container" style="height: calc(100vh); overflow: hidden;">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { onMounted, provide, useTemplateRef } from 'vue';

import { useElementSize } from '@vueuse/core';
import { useRoute, useRouter } from 'vue-router';

import MainLogo from 'src/components/MainLogo.vue';
import PersonnelCenterTitle from 'src/components/PersonnelCenterTitle.vue';
import CurrentDateTime from 'src/components/CurrentDateTime.vue';
import { usePCStore } from 'src/stores/personalCenter';
import { CHOOSE_PC } from 'src/router/pathName';

const headerEl = useTemplateRef('headerEl')
const { height: headerHeight } = useElementSize(headerEl)

provide('headerHeight', headerHeight)


const route = useRoute()
const router = useRouter()

const pcStore = usePCStore()

onMounted(() => {
  if (route.name != CHOOSE_PC){
    if (pcStore.getEmptyStatus){
      router.push({name: CHOOSE_PC})
    }
  }
})

</script>


<style scoped>
  .main-page-container{
    background-color: #F5F5F5 !important;
  }
</style>