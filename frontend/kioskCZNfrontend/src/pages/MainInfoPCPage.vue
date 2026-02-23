<template>
    <q-page>
        <titel-page 
            :path-name="INFO"
            titel="О кадровом центре"
        />

        <head-info />
    </q-page>
</template>

<script setup>
import { INFO } from 'src/router/pathName';
import TitelPage from 'src/components/TitelPage.vue';
import HeadInfo from 'src/components/infoAboutPC/HeadInfo.vue';
</script>