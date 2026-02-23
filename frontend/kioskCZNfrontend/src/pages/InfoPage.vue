<template>
    <q-page>
        <titel-page ref="titelEl" titel="Важная информация" />
        <div 
            class="row flex flex-center"
            :style="stylePunktMenu"
        >
            <card-menu 
                titel="О кадровом центре"
                icon="info"
            />
            <card-menu
                titel="Документы"
                icon="article"
            />
        </div>

    </q-page>
</template>

<script setup>
import { useWindowSize, useElementSize } from '@vueuse/core';
import { inject, computed, useTemplateRef } from 'vue';

import TitelPage from 'src/components/TitelPage.vue';
import CardMenu from 'src/components/CardMenu.vue';

const {height: windowHeight} = useWindowSize()

const headerHeight = inject('headerHeight')

const titelEl = useTemplateRef('titelEl')
const { height: titelPageHeight} = useElementSize(titelEl)

const stylePunktMenu = computed(() => ({
    height: `${windowHeight.value - (headerHeight.value + titelPageHeight.value)}px`
}))




</script>