<template>
  <q-layout view="lHh Lpr lFf">
    <q-header class="bg-white" elevated>
      <q-toolbar>
        <q-toolbar-title>
          <div class="row items-center">
            <main-logo />
            <personnel-center-title />
          </div>
        </q-toolbar-title>
        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import MainLogo from 'src/components/MainLogo.vue';
import PersonnelCenterTitle from 'src/components/PersonnelCenterTitle.vue';

</script>
