<template>
    <q-page>
        <titel-page titel="СМАРТ-ассистенты" />
        <iframe
            ref="iframeRef"
            :src="assistantUrl"
            :width="windowWidht" 
            :height="windowHeight"
            frameborder="0">
        </iframe>
    </q-page>
</template>

<script setup>
import TitelPage from 'src/components/TitelPage.vue';

import { useWindowSize } from '@vueuse/core';


const {width: windowWidht, height: windowHeight } = useWindowSize()

const assistantUrl = process.env.SMART_ASSISTENT_API
</script>