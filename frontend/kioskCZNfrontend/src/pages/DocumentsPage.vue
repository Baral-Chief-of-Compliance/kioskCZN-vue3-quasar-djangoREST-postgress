<template>
    <q-page>
        <titel-page 
            :path-name="INFO"
            titel="Документы"
        />
    </q-page>
</template>

<script setup>
import { INFO } from 'src/router/pathName';
import TitelPage from 'src/components/TitelPage.vue';
</script>