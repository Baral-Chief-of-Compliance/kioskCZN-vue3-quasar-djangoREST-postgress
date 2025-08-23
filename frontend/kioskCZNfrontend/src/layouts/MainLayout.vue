<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>

          <q-icon name="warning" color="warning" size="4rem" />

        </q-toolbar-title>
        <main-logo color="red" />
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

</script>
