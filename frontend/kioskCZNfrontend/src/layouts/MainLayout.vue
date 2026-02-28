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
import { provide, useTemplateRef, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import { useElementSize } from '@vueuse/core';

import MainLogo from 'src/components/MainLogo.vue';
import PersonnelCenterTitle from 'src/components/PersonnelCenterTitle.vue';
import CurrentDateTime from 'src/components/CurrentDateTime.vue';
import { CHOOSE_PC } from 'src/router/pathName';
import { usePCStore } from 'src/stores/personalCenter';
import { getPersonalCenterData } from 'src/axios/personalCenter';

const headerEl = useTemplateRef('headerEl')
const { height: headerHeight } = useElementSize(headerEl)

provide('headerHeight', headerHeight)


const route = useRoute()
const router = useRouter()


const pcStore = usePCStore()

onMounted(async() => {
  if (route.name != CHOOSE_PC){
    try{
      const res = await getPersonalCenterData(route.params.pc)
      if (res.length > 0){
        pcStore.setStore(res[0])
      }else{
        router.push({name: CHOOSE_PC})
      }
    } catch(err){
      console.error(err)
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