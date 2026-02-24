<template>
    <q-page>
        <titel-page 
            :path-name="INFO"
            titel="Документы"
        />
        <not-found-content height="800px" />
    </q-page>
</template>

<script setup>
import { INFO } from 'src/router/pathName';
import TitelPage from 'src/components/TitelPage.vue';
import NotFoundContent from 'src/components/NotFoundContent.vue';

</script>