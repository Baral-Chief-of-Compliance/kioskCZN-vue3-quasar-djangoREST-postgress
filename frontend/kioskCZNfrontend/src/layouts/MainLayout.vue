<template>
  <q-layout view="lHh Lpr lFf">
    <q-header class="bg-white" elevated>
      <q-toolbar class="row justify-between">
        <q-toolbar-title class="col-2">
            <main-logo />
        </q-toolbar-title>
        <personnel-center-title class="col-8 text-center" />
        <current-date-time class="col-2" />
      </q-toolbar>
    </q-header>
    <q-page-container class="main-page-container">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import MainLogo from 'src/components/MainLogo.vue';
import PersonnelCenterTitle from 'src/components/PersonnelCenterTitle.vue';
import CurrentDateTime from 'src/components/CurrentDateTime.vue';

</script>


<style scoped>
  .main-page-container{
    background-color: #F5F5F5 !important;
  }
</style>